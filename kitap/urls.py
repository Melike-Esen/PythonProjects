from django.contrib import admin
from django.urls import path,include
from . import views
app_name='kitap'

urlpatterns = [
    path('',views.merhaba,name='merhaba')
    path('ekle',views.ekle,name='ekle')
    path('sil/<int:id>',views.sil,name='sil')
]