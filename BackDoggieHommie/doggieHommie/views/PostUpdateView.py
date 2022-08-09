from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from doggieHommie.serializers import PostSerializer
from doggieHommie.models import Post


class PostUpdateView(generics.UpdateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def patch(self, request, pk):
        data = request.data
        post = Post.objects.get(id = pk)
        print(post.title)
        if post.state_user== "ACTIVO":
            data["state_user"] = "INACTIVO"
        else:
            data["state_user"] = "ACTIVO"
        response = super().patch(request)
        return response   

            
    