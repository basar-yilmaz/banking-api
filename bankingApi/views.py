from rest_framework.response import Response
from .models import Customer, BankAccount
from .serializer import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import status
from .utils import perform_transfer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BankAccountListCreateAPIView(ListCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BankAccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class TransferTransactionCreateAPIView(CreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = TransferTransactionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        source_account_number = serializer.validated_data['source_account_number']
        destination_account_number = serializer.validated_data['destination_account_number']
        transfer_amount = serializer.validated_data['transfer_amount']

        success, error_message = perform_transfer(source_account_number, destination_account_number, transfer_amount)

        if success:
            return Response({"message": "Transfer successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
