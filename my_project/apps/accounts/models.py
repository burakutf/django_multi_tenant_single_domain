from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


from my_project.apps.tenant.models import Organization


class User(AbstractUser):
    class Genders(models.TextChoices):
        MAN = 'MN', 'Erkek'
        WOMAN = 'WMN', 'Kadın'

    organization = models.ForeignKey(Organization, models.CASCADE, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=3, choices=Genders.choices, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        return super().save(
            *args, **kwargs
        )   # You should prefer to use concat

    def __str__(self):
        return self.full_name or self.get_full_name() or str(self.id)
