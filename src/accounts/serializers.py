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
