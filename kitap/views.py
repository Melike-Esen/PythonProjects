from django.shortcuts import render,redirect
from.models import Book
from .forms import BookForm

def merhaba(request):
    liste=Book.objects.all()
    return render(request,'kitap/giris.html',{'kitaplar':liste})

def ekle(request):
    if request.method== 'POST':
        form =BookForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form=BookForm
    return render(request,'kitap/ekle.html',{'form':form})

def sil(request,id):
    kayit=Book.objects.get(id=id)
    kayit.delete()
    return redirect('/')
