from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .serializers import UserModelSerializer, CreateUserModelSerializer
from .filters import UserFilterSet

from main_app.utils.permisions import IsAdminUser, IsStaffUser

# Create your views here.


class UserModelViewSet(ModelViewSet):
    """
    crud endoints for User model
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

    # serializer_class = UserModelSerializer
    queryset = User.objects.all()
    filterset_class = UserFilterSet
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        # specify permission for each mehtod
        if self.request.method in ["POST"]:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_serializer_class(self):
        # specify serializer for each method
        if self.request.method in ["POST"]:
            return CreateUserModelSerializer
        return UserModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return_data = serializer.data
        return_data.pop("password")
        return Response(
            return_data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()
