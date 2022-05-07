from rest_framework import serializers
from doggieHommie.models import Post, BankAccounts
from .BankAccountSerializer import BankAccountSerializer


class PostSerializer (serializers.ModelSerializer):
    
    idBankAccount = serializers.PrimaryKeyRelatedField( write_only=True, queryset =BankAccounts.objects.all(),
                                                       source='bankAccounts', many = True )
        
    class Meta:
        model = Post
        fields =  ['title', 'description', 'date', 'grade', 'isDonation', 'state', 'number_banned', 'user', 'bankAccounts', 'idBankAccount']
        read_only_fields = ['bankAccounts']
    
    
        
        
         
