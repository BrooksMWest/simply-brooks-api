"""View module for handling requests about books"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybrooksapi.models import Book
from simplybrooksapi.models import BookGenre
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class BookGenreView(ViewSet):
    """Level up book genre views view"""

    def retrieve(self, request, pk):
        """Handle GET requests for different genres that are on a book

        Returns:
            Response -- JSON serialized genres on a book
        """
        bookGenre = BookGenre.objects.get(pk=pk)
        serializer = BookGenreSerializer(bookGenre)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all books

        Returns:
            Response -- JSON serialized list of books
        """
        bookGenres = BookGenre.objects.all()


        serializer = BookGenreSerializer(bookGenres, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized book instance or error message
        """
        try:
            # Create the book instance with validated data
            bookGenre = BookGenre.objects.create(
                book_id=request.data["book_id"],
                genre_id=request.data["genre_id"],  
            )

            # Serialize and return the new book
            serializer = BookGenreSerializer(bookGenre)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError as e:
        # Handle missing fields
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
        # Handle foreign key errors or other object issues
            return Response({"error": "Books or Genres or related object not found."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
        # Catch-all for any other errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    def update(self, request, pk):
        """Handle PUT requests for the genres on a book

        Returns:
           Response -- Empty body with 204 status code or error message
        """
        try:
            bookGenre = BookGenre.objects.get(pk=pk)
            bookGenre.book_id = request.data["book_id"]
            bookGenre.genre_id = request.data["genre_id"]  # Ensure the key matches your frontend
            bookGenre.save()

            serializer = BookGenreSerializer(bookGenre)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Book.DoesNotExist:
            raise Http404("The Genres on this book can not be found")
        except KeyError as e:
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        bookGenre = BookGenre.objects.get(pk=pk)
        bookGenre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        

class BookGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for book genres
    """
    book = serializers.PrimaryKeyRelatedField(read_only=True)
    genre = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = BookGenre
        fields = ('id','book', 'genre')
