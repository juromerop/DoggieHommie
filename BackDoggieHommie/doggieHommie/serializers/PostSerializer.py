from rest_framework import serializers
from doggieHommie.models import Post, BankAccounts, User, Comment
from .BankAccountSerializer import BankAccountSerializer
from .UserSerializer import UserSerializer
from .CommentSerializer import CommentSerializer


class PostSerializer (serializers.ModelSerializer):
    bankAccounts = BankAccountSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    userData = UserSerializer(read_only=True, source='user')
    user = serializers.PrimaryKeyRelatedField( write_only=True, queryset = User.objects.all())
    
    
    idBankAccount = serializers.PrimaryKeyRelatedField( write_only=True, queryset =BankAccounts.objects.all(),
                                                       source='bankAccounts', many = True )
        
    class Meta:
        model = Post
        fields =  ['id','title', 'description', 'date', 'grade', 'isDonation', 'state', 'number_banned', 
              'user', 'bankAccounts', 'idBankAccount', 'userData', 'images', 'comments', 'state_user']
    
    
        
        
         
