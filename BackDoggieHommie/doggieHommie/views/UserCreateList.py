from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import UserSerializer
from doggieHommie.models import User

class UserCreateListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, resquest, *args, **kwargs):
        resquest.data["estado"] = "HABILITADO"
        resquest.data["number_banned"] = 0  
        return super().post(resquest, *args, **kwargs)
    
        