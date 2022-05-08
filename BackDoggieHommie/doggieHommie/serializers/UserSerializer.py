from rest_framework import serializers
from doggieHommie.models import User
from .UserDjangoSerializer import UserDjangoSerializer
from django.contrib.auth.models import User as UserDjango

class UserSerializer (serializers.ModelSerializer):
    user = UserDjangoSerializer()
    class Meta:
        model = User
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        user = UserDjango.objects.create_user(**validated_data["user"])
        validated_data["user"] = user
        userInstance = User.objects.create(**validated_data)
        return userInstance
    
    