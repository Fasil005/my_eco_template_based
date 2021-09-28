from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^register$', views.register),
    path('registering',views.Register.as_view(),name='registering'),
    path('logingin',views.Login.as_view(),name='logingin')
]