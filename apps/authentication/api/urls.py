from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterAPIView, UserDetailsAPIView

urlpatterns = [
    path("register", RegisterAPIView.as_view(), name="register"),
    path("user", UserDetailsAPIView.as_view(), name="user"),
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("refresh", TokenRefreshView.as_view(), name="refresh-token"),
]
