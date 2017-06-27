from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.create),
    url(r'^books$', views.books),
    url(r'^reviews$', views.reviews),
    url(r'^users$', views.users),
    url(r'^create$', views.create),
    ]
