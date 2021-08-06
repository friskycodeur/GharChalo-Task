from django.contrib.auth import authenticate
from ..models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from .serializers import UserRegistrationSerializer, UserSerializer


def get_token_for_user(user):
    """
    A function that return refresh and access token for user
    """
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegisterAPIView(generics.CreateAPIView):
    """
    A view that handles the user registration
    """

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserDetailView(generics.RetrieveAPIView):
    """
    A view that returns user details from username
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, username):
        queryset = User.objects.filter(username=username)
        user = get_object_or_404(queryset, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(["POST"])
def login(request):
    """
    A view that handles login for users
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response(
            {"error": "Please provide both username and password"},
            status=HTTP_400_BAD_REQUEST,
        )
    user = authenticate(username=username, password=password)
    if not user:
        return Response(
            {"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND
        )
    token = get_token_for_user(user)
    serializer = UserSerializer(user)
    data = serializer.data
    return Response({"data": data}, status=HTTP_200_OK)
