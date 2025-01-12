from django.db import models
from simplybrooksapi.models.author import Author
from simplybrooksapi.models.genre import Genre

class AuthorGenre(models.Model):

  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
