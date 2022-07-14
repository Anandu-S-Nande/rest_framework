from rest_framework import serializers
from watchlist.models import Movie

###################################THIS IS MODELSERIALIZER######################################

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField() #customize the model add extra field inside serailizer.py

    class Meta:
        model = Movie
        fields = '__all__'
        #fields = ['id','name','description']
        #exclude = ['active']  Cannot set both 'fields' and 'exclude' options on serializer MovieSerializer.
    
    def get_len_name(self, object):  #customize the model add extra field inside serailizer.py
        length = len(object.name)
        return length

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should be different")  ##validation by field
        else:
            return data


    def validate_name(self, value):  
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")  ### validation by object
        else:
            return value




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