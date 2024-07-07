from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    biography = models.TextField(verbose_name="Biography")

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name="Author")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name="Book")
    quantity = models.IntegerField(verbose_name="Quantity")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    
    def __str__(self):
        return str(self.book.title)
