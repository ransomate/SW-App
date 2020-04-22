from .models import BlogUser
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm


class UserAuthForm(AuthenticationForm):

    class Meta:
        model = BlogUser
        fields = ('username', 'password', 'captcha',)


class UserUpdateForm(UserChangeForm):
    captcha = CaptchaField()

    class Meta:
        model = BlogUser
        fields = ('first_name', 'last_name', 'email', 'captcha', )

