from django.test import TestCase
from django.urls import reverse


class AmortizationTableViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("amortization-table", kwargs={"pk": 1})
        self.assertEqual(url, "/loans/amortization-table/1/")


class LoanApplicationViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("loan-application")
        self.assertEqual(url, "/loans/loan-application/")


class LoanPaymentViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("loan-payment")
        self.assertEqual(url, "/loans/loan-payment/")


class CreateLoanViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("create-loan")
        self.assertEqual(url, "/loans/create-loan/")


class LoanListViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("loan-list")
        self.assertEqual(url, "/loans/loan-list/")


class LoanDetailViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("loan-detail", kwargs={"pk": 1})
        self.assertEqual(url, "/loans/loan-detail/1/")


class LoanProviderListViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("loan-provider-list")
        self.assertEqual(url, "/loans/loan-provider-list/")


class LoanCustomerListViewViewTests(TestCase):
    def test_url_exists(self):
        url = reverse("loan-customer-list")
        self.assertEqual(url, "/loans/loan-customer-list/")
