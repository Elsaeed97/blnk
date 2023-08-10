from rest_framework import serializers
from .models import CustomUser



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ("username", "password", "email", "role")
        extra_kwargs = {"password": {"write_only": True}, "min_length": 6}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def validate(self, attrs):
        role = attrs.get("role")
        allowed_roles = ["LOAN_PROVIDER", "LOAN_CUSTOMER"]

        if role not in allowed_roles:
            raise serializers.ValidationError(
                "Invalid role. Choose from LOAN_PROVIDER or LOAN_CUSTOMER."
            )

        return attrs

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ("username", "password")
