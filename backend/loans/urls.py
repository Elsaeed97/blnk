from django.urls import path
from . import views

urlpatterns = [
    path('amortization-table/<int:pk>/', views.AmortizationTableView.as_view(), name='amortization-table'),
    path('loan-application/', views.LoanApplicationView.as_view(), name='loan-application'),
    path('loan-payment/', views.LoanPaymentView.as_view(), name='loan-payment'),
    path('create-loan/', views.CreateLoanView.as_view(), name='create-loan'),
    path('loan-list/', views.LoanListView.as_view(), name='loan-list'),
    path('loan-detail/<int:pk>/', views.LoanDetailView.as_view(), name='loan-detail'),
    path('loan-provider-list/', views.LoanProviderListView.as_view(), name='loan-provider-list'),
    path('loan-customer-list/', views.LoanCustomerListView.as_view(), name='loan-customer-list'),
]
