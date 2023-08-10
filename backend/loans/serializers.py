from rest_framework import serializers
from .models import LoanProvider, LoanCustomer, Loan, AmortizationTable
from core.models import CustomUser


# LOAN PROVIDER SERIALIZERS
class AmortizationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmortizationTable
        fields = "__all__"


class LoanProviderSerializer(serializers.ModelSerializer):
    amortization_tables = AmortizationTableSerializer(many=True, read_only=True)

    class Meta:
        model = LoanProvider
        fields = "__all__"


# CUSTOMER SERIALIZERS
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"


class LoanCustomerSerializer(serializers.ModelSerializer):
    loans_taken = LoanSerializer(many=True, read_only=True)

    class Meta:
        model = LoanCustomer
        fields = "__all__"


# BANK PERSONNEL SERIALIZERS
class BankPersonnelLoanProviderSerializer(serializers.ModelSerializer):
    max_loan_amount = serializers.DecimalField(
        source="loans_provider.max_amount",max_digits=10, decimal_places=2, read_only=True
    )
    min_loan_amount = serializers.DecimalField(
        source="loans_provider.min_amount",max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = LoanProvider
        fields = "__all__"


class BankPersonnelSerializer(serializers.ModelSerializer):
    loans_provider = BankPersonnelLoanProviderSerializer(many=True, read_only=True)
    loans_customer = LoanCustomerSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        role = instance.role
        if role == "BANK_PERSONNEL":
            return data
        return None
