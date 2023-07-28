from rest_framework import serializers
from .models import Customer, BankAccount



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name')
        
class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('account_id', 'customer', 'balance')


class TransferTransactionSerializer(serializers.Serializer):
    source_account_number = serializers.IntegerField()
    destination_account_number = serializers.IntegerField()
    transfer_amount = serializers.DecimalField(max_digits=10, decimal_places=2)