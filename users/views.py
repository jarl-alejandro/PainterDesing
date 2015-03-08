from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from .models import User
from .forms import UserRegistrationForm, LoginForm

def user_registration(request):
	if request.method == "POST":
		user_register = UserRegistrationForm(request.POST, request.FILES)
		if user_register.is_valid():
			
			User.objects.create_user(
				email = user_register.cleaned_data['email'],
				password = user_register.cleaned_data['password'],
				nombre = user_register.cleaned_data['nombre'],
				apellido = user_register.cleaned_data['apellido'],
				avatar = user_register.cleaned_data['avatar'])

			email = user_register.cleaned_data['email']
			password = user_register.cleaned_data['password']

			user = authenticate(email = email, password = password)
			if user is not None:
				login(request, user)
				
			return redirect("/")
	else:
		user_register = UserRegistrationForm()
		return render(request, "register.html", { 'user_register':user_register })


def user_login(request):
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		
		if login_form.is_valid():
			email = login_form.cleaned_data['email']
			password = login_form.cleaned_data['password']

			user = authenticate(email = email, password = password)
			if user is not None:
				login(request, user)

			return redirect("/")
	else:
		login_form = LoginForm()
		return render(request, "login.html", { "login_form":login_form })						

def LogOut(request):
	logout(request)
	return redirect("/")

@login_required(login_url = "/login/")
def index(request):
	return render(request, "index.html")