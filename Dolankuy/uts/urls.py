from django.contrib import admin
from django.urls import path


from . import views
from uas.views import *
from pemesanan.views import booking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('pantai/',views.pantai),
    path('service/',views.service),
    path('galeri/',views.galeri),
    path('tampilbrg/',Barang_View),
    path('booking/',booking),
    path('barang/',tambah_barang),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
]
