from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def LogIn(request, email, password):
	user = authenticate(email = email, password = password)
	if user is None:
		if user.is_active:
			login(request, user) 