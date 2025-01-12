from django.db import models

class Genre(models.model):

  genre = models.CharField(max_length=75)
