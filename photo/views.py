from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .mixins import LoginRequired
from .models import Photo
from .forms import UploadPhotoForm

class LandingView(TemplateView):
	template_name = "landing.html"

class App(LoginRequired, TemplateView):
	template_name = "app.html"

	def get_context_data(self, **kwargs):
		context = super(App, self).get_context_data(**kwargs)
		photos = Photo.objects.all()

		data = { 'photos':photos }

		context.update(data)
		return context

class UploadPhotView(LoginRequired, CreateView):
	model = Photo
	form_class = UploadPhotoForm
	template_name = "upload.html"
	success_url = "/app/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UploadPhotView, self).form_valid(form)