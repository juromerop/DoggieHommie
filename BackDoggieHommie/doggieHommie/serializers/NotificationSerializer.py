from rest_framework import serializers
from doggieHommie.models import Notification

class NotificationSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = ['id', 'user', 'text', 'date', 'post']