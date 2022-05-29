from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from doggieHommie.serializers import CommentSerializer
from doggieHommie.models import Comment
from time import time_ns
from datetime import datetime 


class CommentCreateList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['date']
    ordering = ['-date']
    serializer_class = CommentSerializer
    
    
    def post(self, resquest, *args, **kwargs):
        resquest.data["date"] = datetime.now().strftime("%Y-%m-%d")      
        return super().post(resquest, *args, **kwargs)