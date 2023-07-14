import re

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from rest_framework import serializers


def cell_phone_valications(cell_phone):
    """
    check cell phone validations
    """
    string_regex = r"^9\d{9}$"
    match = re.match(string_regex, cell_phone)
    if match is None:
        raise serializers.ValidationError(
            {
                "cell_phone": (
                    f"cell phone '{cell_phone}' is invalid, should be 10 digit"
                    " and start with 9"
                )
            }
        )


def email_validator(email):
    if email:
        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError(
                {"email": f"email '{email}' is invalid"}
            )
        item_list = email.split(".")
        for item in ["com", "net", "ir", "org", "co"]:
            if item_list.count(item) > 1:
                raise serializers.ValidationError(
                    {"email": f"email '{email}' is invalid"}
                )
