from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserModelSerializer
from .filters import UserFilterSet

from main_app.utils.permisions import IsAdminUser, IsStaffUser

# Create your views here.


class UserModelViewSet(ModelViewSet):
    """
    endoint for User model
    """

    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    filterset_class = UserFilterSet

    def get_permissions(self):
        # specify permission for each mehtod
        if self.action in ["POST"]:
            self.permission_classes = [AllowAny]
        elif self.action == ["DELETE", "Get"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
