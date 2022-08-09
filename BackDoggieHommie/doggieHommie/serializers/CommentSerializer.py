from rest_framework import serializers
from doggieHommie.models import Comment, User
from .UserSerializer import UserSerializer


class CommentSerializer (serializers.ModelSerializer):
    
    userData = UserSerializer(read_only=True, source='user')
    user = serializers.PrimaryKeyRelatedField( write_only=True, queryset = User.objects.all())

    class Meta:
        model = Comment
        fields =  ['id','text', 'date', 'post', 'userData', 'user']
    