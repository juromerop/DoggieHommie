from rest_framework import serializers
from doggieHommie.models import Post, BankAccounts, User
from .BankAccountSerializer import BankAccountSerializer
from .UserSerializer import UserSerializer


class PostSerializer (serializers.ModelSerializer):
    bankAccounts = BankAccountSerializer(many=True, read_only=True)
    userData = UserSerializer(read_only=True, source='user')
    user = serializers.PrimaryKeyRelatedField( write_only=True, queryset = User.objects.all())
    
    
    idBankAccount = serializers.PrimaryKeyRelatedField( write_only=True, queryset =BankAccounts.objects.all(),
                                                       source='bankAccounts', many = True )
        
    class Meta:
        model = Post
        fields =  ['title', 'description', 'date', 'grade', 'isDonation', 'state', 'number_banned', 
                   'user', 'bankAccounts', 'idBankAccount', 'userData']
    
    
        
        
         
