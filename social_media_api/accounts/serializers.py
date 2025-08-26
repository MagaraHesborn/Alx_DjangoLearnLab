from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from .models import AccountsUser


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsUser
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = AccountsUser
        fields = ["id", "username", "email", "bio", "profile_picture", "followers", "password", "token"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            bio=validated_data.get("bio", ""),
            profile_picture=validated_data.get("profile_picture", None),
        )
        # Create a token for the new user
        token, created = Token.objects.create(user=user)
        user.token = token.key
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            token, created = Token.objects.create(user=user)
            return {"user": user, "token": token.key}
        raise serializers.ValidationError("Invalid credentials")
