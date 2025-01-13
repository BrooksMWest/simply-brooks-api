"""View module for handling requests about books"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybrooksapi.models import Book
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class BookView(ViewSet):
    """Level up book view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single book

        Returns:
            Response -- JSON serialized book
        """
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all books

        Returns:
            Response -- JSON serialized list of books
        """
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

def create(self, request):
    """Handle POST operations

    Returns:
        Response -- JSON serialized book instance or error message
    """
    try:
        # Create the book instance with validated data
        book = Book.objects.create(
            author_id=request.data["author_id"],
            description=request.data["description"],  # Ensure the key matches your frontend
            image=request.data["image"],
            price=request.data["price"],
            sale=request.data["sale"],
            title=request.data["title"],
            uid=request.data["uid"]
        )

        # Serialize and return the new book
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except KeyError as e:
        # Handle missing fields
        return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    except ObjectDoesNotExist:
        # Handle foreign key errors or other object issues
        return Response({"error": "Author or related object not found."}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        # Catch-all for any other errors
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

def update(self, request, pk):
    """Handle PUT requests for a book

    Returns:
        Response -- Empty body with 204 status code or error message
    """
    try:
        book = Book.objects.create(
        author_id=request.data["author_id"],
        description=request.data["description"],  # Ensure the key matches your frontend
        image=request.data["image"],
        price=request.data["price"],
        sale=request.data["sale"],
        title=request.data["title"],
        uid=request.data["uid"]
        )     
        book.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        raise Http404("Book not found")
    except KeyError as e:
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        


class BookSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Book
        depth =1
        fields = ('author_id', 'description', 'image', 'price', 'sale', 'title', 'uid')
