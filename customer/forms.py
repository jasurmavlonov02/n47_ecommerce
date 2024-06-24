from django import forms

from customer.models import Customer, User


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class LoginForm(forms.Form):
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
            raise forms.ValidationError(f'{email} does not exists')
        return password


# class RegisterModelForm(forms.ModelForm):
#     confirm_password  = forms.CharField()
#     class Meta:
#         model = User
#         fields = ('email', 'password')
#
#     def clean_confirm_password(self):
#         pass
#