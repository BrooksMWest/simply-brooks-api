from django.db import models
from simplybrooksapi.models.author import Author

class Book(models.model):

  author_id = models.CharField(max_length=50)
  description = models.BooleanField()
  image = models.CharField(max_length=150)
  price = models.CharField(max_length=50)
  sale = models.BooleanField()
  title = models.CharField(max_length=50)
  uid = models.CharField(max_length=75)
