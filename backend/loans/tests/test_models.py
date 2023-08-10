from django.test import TestCase
from django.contrib.auth import get_user_model
from loans.models import LoanProvider, LoanCustomer, Loan, AmortizationTable


User = get_user_model()


class LoanProviderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="provider_user", password="provider_password"
        )
        self.loan_provider = LoanProvider.objects.create(
            loan_provider_user=self.user, name="Provider 1", total_funds=100000
        )

    def test_loan_provider_str(self):
        self.assertEqual(str(self.loan_provider), "Provider 1")


class LoanCustomerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="customer_user", password="customer_password"
        )
        self.loan_customer = LoanCustomer.objects.create(
            loan_customer_user=self.user, name="Customer 1"
        )

    def test_loan_customer_str(self):
        self.assertEqual(str(self.loan_customer), "Customer 1")


class LoanTestCase(TestCase):
    def setUp(self):
        self.loan_provider_user = User.objects.create_user(
            username="provider_user", password="provider_password"
        )
        self.loan_provider = LoanProvider.objects.create(
            loan_provider_user=self.loan_provider_user,
            name="Provider 1",
            total_funds=100000,
        )
        self.loan_customer = LoanCustomer.objects.create(
            loan_customer_user=self.loan_provider_user, name="Customer 1"
        )
        self.loan = Loan.objects.create(
            loan_provider=self.loan_provider,
            loan_customer=self.loan_customer,
            amount=5000,
            min_amount=1000,
            max_amount=10000,
            duration=12,
            interest_rate=0.05,
        )

    def test_loan_str(self):
        expected_str = "Loan from Provider 1 to Customer 1"
        self.assertEqual(str(self.loan), expected_str)


class AmortizationTableTestCase(TestCase):
    def setUp(self):
        self.loan_provider_user = User.objects.create_user(
            username="provider_user", password="provider_password"
        )
        self.loan_provider = LoanProvider.objects.create(
            loan_provider_user=self.loan_provider_user,
            name="Provider 1",
            total_funds=100000,
        )
        self.loan_customer = LoanCustomer.objects.create(
            loan_customer_user=self.loan_provider_user, name="Customer 1"
        )
        self.loan = Loan.objects.create(
            loan_provider=self.loan_provider,
            loan_customer=self.loan_customer,
            amount=5000,
            min_amount=1000,
            max_amount=10000,
            duration=12,
            interest_rate=0.05,
        )
        self.amortization_table = AmortizationTable.objects.create(
            loan=self.loan,
            installment_number=1,
            payment_date="2023-08-15",
            principal=4500,
            interest=250,
            total_payment=4750,
        )

    def test_amortization_table_str(self):
        expected_str = "Amortization for Loan Loan from Provider 1 to Customer 1"
        self.assertEqual(str(self.amortization_table), expected_str)
