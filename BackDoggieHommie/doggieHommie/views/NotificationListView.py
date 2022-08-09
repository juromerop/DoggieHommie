from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import NotificationSerializer
from doggieHommie.models import Notification, User, Post

class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        posts = Post.objects.filter(user = user)
        noti = []
        if posts:
            for post in posts:
                notifications = Notification.objects.filter(post = post)
                if notifications:
                    for notification in notifications:
                        noti.append(notification)
        return noti