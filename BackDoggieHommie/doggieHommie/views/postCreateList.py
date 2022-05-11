from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import PostSerializer
from doggieHommie.models import Post


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(state = "HABILITADO")
    serializer_class = PostSerializer
    
    def post(self, resquest, *args, **kwargs):      
        return super().post(resquest, *args, **kwargs)
    
        
                 