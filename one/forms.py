from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from django.contrib.auth import validators
from django.forms import ValidationError,ModelForm
from .models import *





class Regform(ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','password']


class revform(ModelForm):
    class Meta:
        model=Userreview
        fields='__all__'

class crevform(ModelForm):
    class Meta:
        model=Criticreview
        fields='__all__'