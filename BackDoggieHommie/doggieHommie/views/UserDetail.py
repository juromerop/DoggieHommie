from cgitb import lookup
from multiprocessing import context
from doggieHommie.models import User
from doggieHommie.serializers import UserSerializer
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class UserDetailAPIView(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)  
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        print(user)
        print(request.data)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    
#     serializer_class  = UserSerializer
#     lookup_url_kwarg  = "id"

#     queryset = User.objects.get(id=id)

    # def get_queryset(self):
    #     return User.objects.filter(user=self.request.user)





        


