from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.response   import TemplateResponse

def home(request):
    return render(request,"web/post/index.html")

