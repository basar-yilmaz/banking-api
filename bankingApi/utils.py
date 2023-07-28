from .models import BankAccount
from django.db import transaction

def perform_transfer(source_account_number, destination_account_number, transfer_amount):
    try:
        # Retrieve the source and destination bank accounts
        source_account = BankAccount.objects.get(account_id=source_account_number)
        destination_account = BankAccount.objects.get(account_id=destination_account_number)
        
        if (source_account_number == destination_account_number):
            return False, "Source and destination account numbers cannot be the same."

        # Ensure the source account has enough balance for the transfer
        if source_account.balance < transfer_amount:
            return False, "Insufficient balance in the source account."

        # Perform the transfer
        source_account.balance -= transfer_amount
        destination_account.balance += transfer_amount

        # Save changes to the database in an atomic transaction
        with transaction.atomic():
            source_account.save()
            destination_account.save()

        return True, None  # Successful transfer

    except BankAccount.DoesNotExist:
        return False, "One or both account numbers are invalid."

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error occurred during transfer: {str(e)}")

        # Return a more descriptive error message
        return False, "An error occurred while processing the transfer. Please contact support."
