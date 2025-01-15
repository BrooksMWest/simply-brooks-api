from django.db import models
from .author import Author
class Book(models.Model):

  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  description = models.TextField()
  image = models.CharField(max_length=150)
  price = models.CharField(max_length=50)
  sale = models.BooleanField()
  title = models.CharField(max_length=50)
  uid = models.CharField(max_length=75)
