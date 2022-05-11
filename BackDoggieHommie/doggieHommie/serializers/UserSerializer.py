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
    
    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.telefono = validated_data.get('telefono', instance.telefono)
    #     instance.pais = validated_data.get('pais', instance.pais)
    #     instance.ciudad = validated_data.get('ciudad', instance.ciudad)
    #     instance.estado = validated_data.get('estado', instance.estado)
        
    #     instance.save()
    #     return instance
    
    