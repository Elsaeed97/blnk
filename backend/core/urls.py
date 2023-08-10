from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomAuthToken, UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("login/", CustomAuthToken.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
