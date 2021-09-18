from django import forms
from django.contrib.auth.models import User
from .models import location
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


class locationForm(forms.ModelForm):
	class Meta:
		model = location
		fields = ['location']

