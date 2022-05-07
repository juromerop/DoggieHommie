from rest_framework import serializers
from doggieHommie.models import Post
from .BankAccountSerializer import BankAccountSerializer


class PostSerializer (serializers.ModelSerializer):
    
    bankAccounts = BankAccountSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'
    
    
        
        
         
