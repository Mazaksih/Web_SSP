from django.shortcuts import render
from django.conf.urls.static import static

# Ini adalah method yang digunakan untuk memanggil data dari file index.html
def index(request):
    return render(request,'index.html')

def pantai(request):
    return render(request,'pantai.html')

def service(request):
    return render(request,'service.html')

def galeri(request):
    return render(request,'galeri.html')

