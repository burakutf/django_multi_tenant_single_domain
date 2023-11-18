from rest_framework import viewsets

from my_project.api.accounts.serializers import (
    UserSerializers,
)
from my_project.apps.accounts.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    search_fields = (
        'username',
        'full_name',
        'phone',
        'email',
    )
