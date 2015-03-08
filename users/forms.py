from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("email", "password" ,"nombre", "apellido", "avatar")
		widgets = {
			'email' : forms.TextInput(attrs = 
			{
				'class' : "emailRegistration",
				'placeholder' : "Ingresa un email",
				'type' : "email",
			}),

			"password" :  forms.TextInput(attrs = 
			{
				'class' : "passwordRegistratio",
				'placeholder':"Ingresa un password",
				'type': "password"
			}),
		}

class LoginForm(forms.Form):
	email = forms.CharField(max_length = 200, 
		widget = forms.TextInput(attrs = {
			'class' : "emailLogin",
			'type': "email"
		}))

	password = forms.CharField(max_length = 200, 
		widget = forms.TextInput(attrs = {
			'class' : "passwordLogin",
			'type' : "password"
		}))