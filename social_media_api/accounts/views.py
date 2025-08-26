from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import login

from .models import AccountsUser
from .serializers import RegisterSerializer, LoginSerializer, AccountUserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = AccountsUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = AccountsUser.objects.get(id=response.data["id"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": AccountUserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            "user": AccountUserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_200_OK)
# Create your views here.
