from django.conf.urls import url
from django.contrib import admin
from . import views




urlpatterns = [

    url(r'^$', views.index, name='index'),
    # url(r'^hello/$', views.index, name='hello'), no more "hello function"
    url(r'^(?P<doctor_id>[0-9]+)/$', views.doctor, name='doctor'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^doctors/$', views.doctor_list),
    url(r'^doctors/(?P<pk>[0-9]+)/$', views.doctor_detail),
    url(r'^doctors/(?P<pk>[0-9]+)/edit/$', views.doctor_detail),




]
