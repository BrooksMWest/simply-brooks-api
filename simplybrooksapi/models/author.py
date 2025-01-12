from django.db import models

class Author(models.model):

  email = models.CharField(max_length=75)
  favorite = models.BooleanField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  uid = models.CharField(max_length=75)
