from django.contrib import admin
from django.urls import path,include
from .forms import BookForm
from.models import Book
from . import  views
app_name='dizi'
urlpatterns = [
    path('',views.merhaba,name='merhaba'),
    path('ekle', views.ekle, name='ekle'),
    path('sil/<int:id>', views.sil, name='sil')

]

