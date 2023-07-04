from django.shortcuts import render, redirect
from uas.forms import FormBarang
from uas.models import Barang
from django.contrib import messages


def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def tambah_barang(request):
    form = FormBarang(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form = FormBarang()
        konteks = {
            'form' : form,
        }
        return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form' : form,
        }
    return render(request,'tambah_barang.html',konteks)

def ubah_brg(request,id_barang) :
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil di ubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data terhapus")
    return redirect('/tampilbrg')