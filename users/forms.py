from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("email", "password" ,"nombre", "apellido", "avatar")
		widgets = {
			'email' : forms.TextInput(attrs = {
				'class' : "emailRegistration",
				'placeholder' : "Ingresa un email",
				'type' : "email",
			}),

			"password" :  forms.TextInput(attrs = {
				'class' : "passwordRegistratio",
				'placeholder':"Ingresa un password",
				'type': "password"
			}),
			'nombre' : forms.TextInput(attrs = {
				'class' : "nombreRegistration",
				'placeholder' : "Ingresa un nombre"
			}),

			"apellido" :  forms.TextInput(attrs = {
				'class' : "apellidoRegistratio",
				'placeholder':"Ingresa un apellido"
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