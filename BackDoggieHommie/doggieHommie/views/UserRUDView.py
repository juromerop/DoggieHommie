from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import UserSerializer
from doggieHommie.models import User

class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer