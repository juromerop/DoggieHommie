from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from doggieHommie.serializers import CommentSerializer
from doggieHommie.models import Comment, Notification, User, Post
from django.contrib.auth.models import User as DjangoUser
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
        post = Post.objects.get(id = resquest.data["post"])
        user = User.objects.get(id = int(resquest.data["user"]))
        userApp = DjangoUser.objects.get(id = user.user_id)
        print(userApp.username)
        notification = Notification( 
                                    user = user,
                                    text = "El usuario "+ userApp.first_name+" ha comentado en tu post:  "+post.title,
                                    date = datetime.now().strftime("%Y-%m-%d"),
                                    post = post)
        notification.save()      
        return super().post(resquest, *args, **kwargs)