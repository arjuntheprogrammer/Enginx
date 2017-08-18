from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^position/$', views.position, name="position"),
    url(r'^position2/$', views.position2, name="position2"), 
]
