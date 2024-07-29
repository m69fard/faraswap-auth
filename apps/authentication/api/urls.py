from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterAPIView, UserDetailsAPIView

urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("user", UserDetailsAPIView.as_view()),
    path("login", TokenObtainPairView.as_view(), name="access-token"),
    path("refresh", TokenRefreshView.as_view(), name="refresh-token"),
]


