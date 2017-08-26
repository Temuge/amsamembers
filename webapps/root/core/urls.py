from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root', settings.STATIC_ROOT}),
    url(r'^$', views.index, name='index'),
    url(r'^submitRegistration/$', views.submitRegistration, name='submitRegistration'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^confirmEmail/(?P<externalId>\w+)/(?P<id>\w+)/$', views.confirmEmail, name='confirmEmail'),
]
