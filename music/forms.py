from django.contrib.auth.models import User
from django import forms

# create new user form class
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta: #info about your class
		model = User
		fields = ['username','email', 'password']

