from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import AccountsUser

class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsUser
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AccountsUser
        fields = ["id", "username", "email", "bio", "profile_picture", "followers", "password"]

    def create(self, validated_data):
         user = AccountsUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            bio=validated_data.get("bio", ""),
            profile_picture=validated_data.get("profile_picture", None),
        )
         return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")