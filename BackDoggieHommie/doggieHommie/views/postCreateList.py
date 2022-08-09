from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from doggieHommie.serializers import PostSerializer
from doggieHommie.models import Post


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(state = "HABILITADO", state_user = "ACTIVO")
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['date', 'grade']
    ordering = ['-date','-grade']
    serializer_class = PostSerializer
    
    
    def post(self, resquest, *args, **kwargs):      
        return super().post(resquest, *args, **kwargs)
    
        
                 