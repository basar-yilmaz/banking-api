from django.contrib import admin
from .models import Customer, BankAccount

admin.site.register(Customer)
admin.site.register(BankAccount)
