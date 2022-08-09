from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import PostSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from doggieHommie.models import Post

class PostByUserView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(state = "HABILITADO")
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['date', 'grade']
    ordering = ['-date','-grade']
    serializer_class = PostSerializer
        
    def get_queryset(self):
        user = self.kwargs['user']
        return Post.objects.filter(user=user)