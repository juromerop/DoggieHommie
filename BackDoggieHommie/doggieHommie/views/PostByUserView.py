from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import PostSerializer
from doggieHommie.models import Post

class PostByUserView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
        
    def get_queryset(self):
        user = self.kwargs['user']
        return Post.objects.filter(user=user)