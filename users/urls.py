from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

from .views import UserCreateAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("payment/", PaymentCreateAPIView.as_view(), name="payment_create"),
]
