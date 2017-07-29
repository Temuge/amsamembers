from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submitRegistration/$', views.submitRegistration, name='submitRegistration'),
]
