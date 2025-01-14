from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybrooksapi.models import Author
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class AuthorView(ViewSet):
    """Level up author view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single author

        Returns:
            Response -- JSON serialized author
        """
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all authors

        Returns:
            Response -- JSON serialized list of authors
        """
        authors = Author.objects.all()

        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized author instance or error message
        """
        try:
            # Create the book instance with validated data
            author = Author.objects.create(
            email=request.data["email"],
            favorite=request.data["favorite"],  # Ensure the key matches your frontend
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            uid=request.data["uid"]
            )     

            # Serialize and return the new book
            serializer = AuthorSerializer(author)
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
            author = Author.objects.create(
            email=request.data["email"],
            favorite=request.data["favorite"],  # Ensure the key matches your frontend
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            uid=request.data["uid"]
            )     
            author.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            raise Http404("Author not found")
        except KeyError as e:
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for authors
    """
    class Meta:
        model = Author
        depth =1
        fields = ('id', 'email', 'favorite', 'first_name', 'last_name', 'uid')
