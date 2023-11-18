from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Organization(TenantMixin):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)


class Domain(DomainMixin):
    pass
