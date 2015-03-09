from django.conf.urls import patterns, include, url

from .views import LandingView, App

urlpatterns = patterns('',
	url(r'^$', LandingView.as_view(), name="landing"),
	url(r'^app/$', App.as_view(), name="app"),
)