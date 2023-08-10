from rest_framework import permissions


class HasGroupPermission(permissions.BasePermission):
    def __init__(self, group_name):
        self.group_name = group_name

    def has_permission(self, request, view):
        return request.user.groups.filter(name=self.group_name).exists()


class IsLoanProvider(HasGroupPermission):
    def __init__(self):
        super().__init__("LOAN_PROVIDER")


class IsLoanCustomer(HasGroupPermission):
    def __init__(self):
        super().__init__("LOAN_CUSTOMER")


class IsBankPersonnel(HasGroupPermission):
    def __init__(self):
        super().__init__("BANK_PERSONNEL")
