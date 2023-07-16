from rest_framework import serializers

from .models import User

from main_app.utils.validators import (
    cell_phone_valications,
    email_validator,
)


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "is_removed"]

    def validate(self, attrs):
        cell_phone = attrs.get("cell_phone")
        email = attrs.get("email")
        cell_phone_valications(cell_phone)
        email_validator(email)
        return super().validate(attrs)


class CreateUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "cell_phone", "password"]

    def validate(self, attrs):
        cell_phone = attrs.get("cell_phone")
        email = attrs.get("email")
        cell_phone_valications(cell_phone)
        email_validator(email)
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
