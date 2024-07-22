from django import forms
from customer.custom_field import MultiEmailField
from customer.authentication import AuthenticationForm
from customer.models import Customer, User


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class LoginForm(AuthenticationForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not exist')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.data.get('password')
        try:
            user = User.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except User.DoesNotExist:
            raise forms.ValidationError(f'User does not exists')
        return password


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The {email} is already registered')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password didn\'t match')
        return password


class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ()


class MyCustomField(forms.MultiValueField):

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(max_length=31),
            forms.CharField(max_length=31),
            forms.CharField(max_length=31),
        )
        super(MyCustomField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return "-".join(data_list)


class ShareMail(forms.Form):
    subject = forms.CharField(max_length=125)
    body = forms.CharField(widget=forms.Textarea())
    recipients = MultiEmailField(widget=forms.Textarea())
