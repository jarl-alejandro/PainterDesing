from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'users.views.index', name='index'),
    url(r'^login/$', 'users.views.user_login', name='login'),
    url(r'^logout/$', 'users.views.LogOut', name='logout'),
    url(r'^register/$', 'users.views.user_registration', name='register'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
