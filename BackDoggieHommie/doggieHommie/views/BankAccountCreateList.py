from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import BankAccountSerializer
from doggieHommie.models import BankAccounts


class BankAccountCreateListView(generics.ListCreateAPIView):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountSerializer
    