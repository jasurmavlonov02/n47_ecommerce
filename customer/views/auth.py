from django.contrib import messages
from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView, CreateView

from customer.forms import LoginForm, RegisterModelForm
from django.contrib.auth.decorators import permission_required
from config import settings
from customer.models import User
from customer.views.tokens import account_activation_token


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customers')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


def logout_page(request):
    if request.method == 'GET':
        logout(request)
        return redirect('customers')
    return render(request, 'auth/logout.html')


permission = 'customer.add_customer'


def register_page(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.is_active = False

            user.set_password(password)
            user.save()

            current_site = get_current_site(request)

            subject = "Verify Email"
            message = render_to_string('email/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(subject, message, to=[email])
            email.content_subtype = 'html'

            email.send()
            # login(request, user)
            return redirect('verify_email_done')

        # send

    else:
        form = RegisterModelForm()

    return render(request, 'auth/register.html', {'form': form})


class LoginPageView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customers')

        return render(request, 'auth/login.html', {'form': form})


class LoginPage(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm

    # success_url = reverse_lazy('customers')

    def get_success_url(self):
        return reverse_lazy('customers')


class RegisterFormView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterModelForm

    # success_url = reverse_lazy('customers')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.is_active = False
        user.save()


        current_site = get_current_site(self.request)

        subject = "Verify Email"
        message = render_to_string('email/verify_email_message.html', {
            'request': self.request,
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(subject, message, to=[user.email])
        email.content_subtype = 'html'

        email.send()
        # login(self.request, user)
        return redirect('verify_email_done')


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print('-------------------------------')
        print(user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Your email has been verified.')
        return redirect('customers')
    else:
        messages.warning(request, 'The link is invalid.')

    return render(request, 'email/verify_email_confirm.html')


def verify_email_done(request):
    return render(request, 'email/verify_email_done.html')
