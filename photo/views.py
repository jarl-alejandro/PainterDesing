from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from .mixins import LoginRequired
from .models import Photo
from .forms import UploadPhotoForm

class LandingView(TemplateView):
	template_name = "landing.html"

class App(LoginRequired, ListView):
	model = Photo
	template_name = "app.html"
	context_object_name = "photos" 

class UploadPhotView(LoginRequired, CreateView):
	model = Photo
	form_class = UploadPhotoForm
	template_name = "upload.html"
	success_url = "/app/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UploadPhotView, self).form_valid(form)

class Profile(LoginRequired, TemplateView):
        template_name = "profile.html"
