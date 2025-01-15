"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybrooksapi.models import Genre
from django.core.exceptions import ObjectDoesNotExist


class GenreView(ViewSet):
    """Level up genres view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single genre
      
        Returns:
            Response -- JSON serialized genre
        """
        try:
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
   
    def list(self, request):
        """Handle GET requests to get all genres

        Returns:
            Response -- JSON serialized list of genres
        """
        game_types = Genre.objects.all()
        serializer = GenreSerializer(game_types, many=True)
        return Response(serializer.data)
    

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized genre instance or error message
        """
        try:
            # Create the book instance with validated data
            genre = Genre.objects.create(
                genre = request.data["genre"],
            )

            # Serialize and return the new book
            serializer = GenreSerializer(genre)
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
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        genre = Genre.objects.get(pk=pk)
        genre.genre = request.data["genre"]

        genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        event = Genre.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genres
    """
    class Meta:
        model = Genre
        fields = ('id', 'genre')
