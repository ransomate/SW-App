from django import forms
from .models import BlogUser
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(User):
    captcha = CaptchaField()

    class Meta:
        model = BlogUser
        fields = ['first_name', 'last_name', 'email', 'captcha']


'''
class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
'''


class UpdateUser(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = BlogUser
        fields = ['first_name', 'last_name', 'email', 'captcha']
