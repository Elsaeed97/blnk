from rest_framework import generics
from .serializers import (
    AmortizationTableSerializer,
    LoanCustomerSerializer,
    LoanProviderSerializer,
    LoanSerializer,
)
from .models import AmortizationTable, Loan, LoanCustomer, LoanProvider
from .permissions import IsBankPersonnel, IsLoanCustomer, IsLoanProvider
from rest_framework.permissions import IsAuthenticated
from core.models import CustomUser


class AmortizationTableView(generics.RetrieveAPIView):
    serializer_class = AmortizationTableSerializer
    permission_classes = [IsLoanProvider]
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user
        if user.role == CustomUser.ROLE_CHOICES.LOAN_PROVIDER:
            related_field_name = "loanprovider"
            if hasattr(user, related_field_name):
                return AmortizationTable.objects.filter(
                    loan__loan_provider__loan_provider_user=user
                )
        return AmortizationTable.objects.none()


class LoanApplicationView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsLoanCustomer]

    def perform_create(self, serializer):
        loan_customer = self.request.user.loancustomer
        serializer.save(loan_customer=loan_customer)


class LoanPaymentView(generics.UpdateAPIView):
    serializer_class = AmortizationTableSerializer
    permission_classes = [IsAuthenticated, IsLoanCustomer]

    def get_queryset(self):
        loan_customer = self.request.user.loancustomer
        return AmortizationTable.objects.filter(loan__loan_customer=loan_customer)


class CreateLoanView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsBankPersonnel]

    def perform_create(self, serializer):
        serializer.save()


class LoanListView(generics.ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsBankPersonnel]

    def get_queryset(self):
        return Loan.objects.all()


class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsBankPersonnel]

    def get_queryset(self):
        return Loan.objects.all()


class LoanProviderListView(generics.ListAPIView):
    serializer_class = LoanProviderSerializer
    permission_classes = [IsAuthenticated, IsBankPersonnel]

    def get_queryset(self):
        return LoanProvider.objects.all()


class LoanCustomerListView(generics.ListAPIView):
    serializer_class = LoanCustomerSerializer
    permission_classes = [IsAuthenticated, IsBankPersonnel]

    def get_queryset(self):
        return LoanCustomer.objects.all()
