from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import BankAccountSerializer
from doggieHommie.models import BankAccounts


class BankAccountCreateListView(generics.ListCreateAPIView):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountSerializer
    
    
    def get_queryset(self):
        
        user = self.kwargs.get('pk', None)
        if user is not None:
            return BankAccounts.objects.filter(user=user)
        return BankAccounts.objects.all()
        
    #prueba
    
    
    