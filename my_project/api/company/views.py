from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils.translation import gettext as _

from my_project.apps.company.models import (
    Company,
)

from .serializers import (
    CompanySerializers,
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    search_fields = (
        'name',
        'contact_info',
    )

    @action(detail=False, methods=['get'], url_path='minimal')
    def minimal(self, request):
        queryset = self.get_queryset().values('id', 'name')
        return Response(list(queryset))
