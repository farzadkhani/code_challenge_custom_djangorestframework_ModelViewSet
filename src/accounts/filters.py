from django_filters import rest_framework as filters
from accounts.models import User


class UserFilterSet(filters.FilterSet):
    """
    define filters for User models instances
    """

    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["password"]
