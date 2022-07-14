from rest_framework import serializers
from watchlist.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        field = "__all__"




##############################THIS IS SERIALIZER.SERIALIZER####################################

# class MovieSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)  #this is for POST method

#     def update(self, instance, validated_data): ## this is for PUT method
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('cative', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should be different")  ##validation by field
#         else:
#             return data


#     def validate_name(self, value):  
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")  ### validation by object
#         else:
#             return value