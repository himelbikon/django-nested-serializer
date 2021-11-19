from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class UniverseView(APIView):
    def get(self, request):
        universes = Universe.objects.all()
        serializer = UniverseSerializer(universes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniverseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        universe = Universe.objects.get(pk=pk)
        universe.delete()
        return Response({'message': 'success!'})


class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
