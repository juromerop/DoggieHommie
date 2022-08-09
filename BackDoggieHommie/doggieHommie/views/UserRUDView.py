from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import UserSerializer
from doggieHommie.serializers import UserDjangoSerializer
from doggieHommie.models import User
from django.contrib.auth.models import User as DjangoUser
from rest_framework.response import Response
from rest_framework.status import *

class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def patch(self, request, pk):
        data = request.data
        user = User.objects.get(id = pk)
        if user != None:
            appUser = DjangoUser.objects.get(id = user.user_id)
            data["number_banned"] = int(str(user.number_banned)) + 1
            if int(data["number_banned"]) >= 3:
                data["estado"] = "BLOQUEADO"
                appUser.is_active = False
                appUser.save()
                answer = Response(data={"exitoso": True, "mensaje":"El usuario alcanzo el máximo de reportes. Usuario bloqueado", }, status=HTTP_200_OK)
            else:
                data["estado"] = "HABILITADO"
                answer = Response(data={"exitoso": True, "mensaje":"El usuario fue reportado", }, status=HTTP_200_OK)
            response = super().patch(request)
        return answer