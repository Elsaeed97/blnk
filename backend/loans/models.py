from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LoanProvider(models.Model):
    loan_provider_user = models.OneToOneField(User, related_name="loanprovider", on_delete=models.CASCADE)
    name = models.CharField("Loan Provider Name", max_length=100)
    total_funds = models.DecimalField("Total Funds", max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class LoanCustomer(models.Model):
    loan_customer_user = models.OneToOneField(User, related_name="loancustomer", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Loan(models.Model):
    loan_provider = models.ForeignKey(
        LoanProvider, on_delete=models.CASCADE, related_name="loans_provider"
    )
    loan_customer = models.ForeignKey(
        LoanCustomer, on_delete=models.CASCADE, related_name="loans_customer"
    )
    amount = models.DecimalField("Loan Amount", max_digits=10, decimal_places=2)
    min_amount = models.DecimalField(
        "Minimum Loan Amount", max_digits=10, decimal_places=2
    )
    max_amount = models.DecimalField(
        "Maximum Loan Amount", max_digits=10, decimal_places=2
    )
    duration = models.PositiveIntegerField("Loan Duration in months")
    interest_rate = models.DecimalField("Interest Rate", max_digits=5, decimal_places=2)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    def amount_in_range(self, amount):
        return self.min_amount <= amount <= self.max_amount

    def __str__(self):
        return f"Loan from {self.loan_provider} to {self.loan_customer}"


class AmortizationTable(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    installment_number = models.PositiveIntegerField("Installment Numbers")
    payment_date = models.DateField("Payment Date")
    principal = models.DecimalField("Principal Value", max_digits=10, decimal_places=2)
    interest = models.DecimalField("Interst", max_digits=10, decimal_places=2)
    total_payment = models.DecimalField(
        "Total Payment", max_digits=10, decimal_places=2
    )

    def __str__(self):
        return f"Amortization for Loan {self.loan}"

    @property
    def total_amount(self):
        return self.principal + self.interest

    def calculate_interest(self):
        loan = self.loan
        interest_rate = loan.interest_rate
        duration = loan.duration
        principal = self.principal
        interest = principal * interest_rate * duration / 12
        return interest

    def save(self, *args, **kwargs):
        if not self.interest:
            self.interest = self.calculate_interest()
        super().save(*args, **kwargs)
