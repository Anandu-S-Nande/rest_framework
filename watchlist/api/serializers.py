
from rest_framework import serializers
from watchlist.models import Movie


class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)  #this is for POST method

    def update(self, instance, validated_data): ## this is for PUT method
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('cative', instance.active)
        instance.save()
        return instance