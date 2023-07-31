from django.contrib import admin
from django.urls import path
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.views.generic import TemplateView


urlpatterns = [
    #Swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    
    path('admin/', admin.site.urls),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),
    path('bankaccounts/', BankAccountListCreateAPIView.as_view(), name='bankaccounts-list-create'),
    path('bankaccounts/<int:pk>/', BankAccountRetrieveUpdateDestroyAPIView.as_view(), name='bankaccounts-retrieve-update-destroy'),
    path('transactions/transfer/', TransferTransactionCreateAPIView.as_view(), name='transfer-transaction-create'),
    
]
