from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^login/$', 'users.views.user_login', name='login'),
    url(r'^logout/$', 'users.views.LogOut', name='logout'),
    url(r'^register/$', 'users.views.user_registration', name='register'),
)