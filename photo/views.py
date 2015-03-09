from django.shortcuts import render
from django.views.generic import TemplateView

from .mixins import LoginRequired

class LandingView(TemplateView):
	template_name = "landing.html"

class App(LoginRequired, TemplateView):
	template_name = "app.html"