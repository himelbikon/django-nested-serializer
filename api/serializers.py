from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'universe']
        read_only_fields = ('universe',)


class UniverseSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Universe
        fields = ['id', 'name', 'movies']

    def create(self, validated_data):
        movies = validated_data.pop('movies')
        universe = Universe.objects.create(**validated_data)

        for movie in movies:
            Movie.objects.create(**movie, universe=universe)

        return universe
