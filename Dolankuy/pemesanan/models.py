from django.db import models

class Package(models.Model):
    nama=models.CharField(max_length=50)
    harga=models.BigIntegerField()

    def __str__(self):
        return self.nama

class Booking(models.Model):
    nama=models.CharField(max_length=50)
    package_id=models.ForeignKey(Package, on_delete=models.CASCADE,null=True)
    jmltiket=models.IntegerField()

    def __str__(self):
        return format(self.nama)
