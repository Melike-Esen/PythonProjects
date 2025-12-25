from django.contrib import admin
from django.urls import path,include
from .forms import YerFrom
from.models import Yer
from . import  views
app_name='yerler'
urlpatterns = [
    path('',views.merhaba,name='merhaba'),
    path('ekle', views.ekle, name='ekle'),
    path('sil/<int:id>', views.sil, name='sil')

]

