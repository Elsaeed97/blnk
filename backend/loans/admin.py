from django.contrib import admin
from .models import LoanProvider, LoanCustomer, Loan, AmortizationTable


@admin.register(LoanProvider)
class LoanProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "loan_provider_user", "total_funds")


@admin.register(LoanCustomer)
class LoanCustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "loan_customer_user")


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "loan_provider",
        "loan_customer",
        "amount",
        "min_amount",
        "max_amount",
        "duration",
        "interest_rate",
        "created_at",
    )
    list_filter = (
        "loan_provider",
        "loan_customer",
        "duration",
        "amount",
        "interest_rate",
    )


@admin.register(AmortizationTable)
class AmortizationTableAdmin(admin.ModelAdmin):
    list_display = (
        "loan",
        "installment_number",
        "payment_date",
        "principal",
        "interest",
        "total_payment",
    )
    list_filter = ("loan", "payment_date")
