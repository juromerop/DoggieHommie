from rest_framework import serializers
from doggieHommie.models import BankAccounts


class BankAccountSerializer (serializers.ModelSerializer):
    class Meta:
        model = BankAccounts
        fields = '__all__'

