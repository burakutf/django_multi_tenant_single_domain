from django.conf import settings

from django_tenants.utils import connection


from django.conf import settings
from django.core.exceptions import DisallowedHost
from django.db import connection
from django_tenants.middleware.main import TenantMainMiddleware
from django_tenants.utils import get_tenant_domain_model


class CustomTenantMainMiddleware(TenantMainMiddleware):
    def get_tenant(self, domain_model, hostname, request):
        if request.user.is_authenticated:
            return request.user.organization

        else:
            domain = domain_model.objects.select_related('tenant').get(
                domain=settings.DOMAIN
            )
            return domain.tenant

    def process_request(self, request):
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.

        connection.set_schema_to_public()
        try:
            hostname = self.hostname_from_request(request)
        except DisallowedHost:
            from django.http import HttpResponseNotFound

            return HttpResponseNotFound()

        domain_model = get_tenant_domain_model()
        try:
            tenant = self.get_tenant(domain_model, hostname, request)
        except domain_model.DoesNotExist:
            self.no_tenant_found(request, hostname)
            return
        tenant.domain_url = hostname
        request.tenant = tenant
        connection.set_tenant(request.tenant)
        self.setup_url_routing(request)


class TenantMediaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_name = request.tenant.name
        settings.MEDIA_URL = f'/media/{tenant_name}/'

        response = self.get_response(request)

        return response
