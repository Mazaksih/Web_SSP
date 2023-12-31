from django.db import models

    
     
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}".format(self.kodebrg,self.nama)
        
class Paket(models.Model):
    nama=models.CharField(max_length=50)
    harga=models.BigIntegerField()

    def __str__(self):
            return self.nama
    
class Pesan(models.Model):
     nama=models.CharField(max_length=50)
     jmltiket=models.IntegerField()
     paket_id=models.ForeignKey(Paket, on_delete=models.CASCADE,null=True)

     def __str__(self):
        return format(self.nama)