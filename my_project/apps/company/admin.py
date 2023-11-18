from django.contrib import admin
from my_project.apps.company.models import (
    Company,
)


admin.site.register(Company)
