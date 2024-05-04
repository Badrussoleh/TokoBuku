from django.db import models

# Create your models here.
class Book(models.Model):
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)

    def __str__(self):
        return self.judul

class Author(models.Model):
    nama = models.CharField(max_length=200)
    biodata = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
    
class Order(models.Model):
    buku = models.CharField(max_length=200)
    jumlah = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

    def __str__(self):
        return self.buku