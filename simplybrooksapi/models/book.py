from django.db import models
class Book(models.Model):

  author_id = models.CharField(max_length=50)
  description = models.TextField()
  image = models.CharField(max_length=150)
  price = models.CharField(max_length=50)
  sale = models.BooleanField()
  title = models.CharField(max_length=50)
  uid = models.CharField(max_length=75)
