from django import forms
# from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

from register.models import Profile
# from .models import Profile

class RegisterForm(UserCreationForm):
  email = models.EmailField()

  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):  
  email = models.EmailField()

  class Meta:
      model = User
      fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ['image']