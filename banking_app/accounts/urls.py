from django.urls import path
from . import views

urlpatterns = [
    path('<int:account_id>/summary/', views.account_summary, name='account_summary'),
    path('<int:account_id>/transfer/', views.transfer_funds, name='transfer_funds'),
    path('<int:account_id>/pay_bill/', views.pay_bill, name='pay_bill'),
    path('<int:account_id>/transaction_history/', views.transaction_history, name='transaction_history'),
    
]
