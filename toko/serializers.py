from rest_framework import serializers
from .models import judul, penulis, harga

# buat kelas serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = judul
        fields = ["judul", "penulis", "harga"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = penulis
        fields = ["nama", "biodata"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = harga
        fields = ["buku", "jumlah", "total"]
        