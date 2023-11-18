from django.contrib import admin

from my_project.apps.tenant.models import Domain, Organization

# Register your models here.
admin.site.register(Organization)
admin.site.register(Domain)
