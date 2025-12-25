from django.http.response import HttpResponse 
from django.shortcuts import render

def anaSayfa(request):
    return render(request,"anaSayfa.html")
def mouse(request):
 return render(request,"mouse.html")
def mouse2(request):
 return render(request,"mouse2.html")
