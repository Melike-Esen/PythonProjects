from django.urls import path
from . import views
urlpatterns=[
path("", views.anaSayfa),
path("anaSayfa", views.anaSayfa),
path("mouse", views.mouse),
path("mouse2", views.mouse2),


]