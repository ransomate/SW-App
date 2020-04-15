from django.db import models
from django import forms
from django.contrib.auth.models import User
form django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
email = models.EmaiField(required=True)

class Meta:
model = User
fields = [
'username',
'first_name',
'last_name',
'email',
'passwor1',
'password2',
]

def save(self, commit=True):
  user = super(RegistrationForm, self).save(commit=False)
user.first_name = cleaned_data['first_name']
user.last_name = self.cleaned_data['last_name']
user.email =self. cleaned_data['email']
if commit:
 user.save()

return user
# Create your models here.
