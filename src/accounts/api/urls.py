from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import path, include
from .views import (
    UserRegisterAPIView,
    UserDetailView,
    login,
)

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserRegisterAPIView.as_view()),
    path("users/<username>", UserDetailView.as_view()),
    path("login/", login),
    path("token/refresh/", TokenRefreshView.as_view()),
]
