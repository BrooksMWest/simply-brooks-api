from django.db import models
from simplybrooksapi.models.book import Book
from simplybrooksapi.models.genre import Genre

class BookGenre(models.Model):

  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
