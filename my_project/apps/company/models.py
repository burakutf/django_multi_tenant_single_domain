from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    tax_number = models.CharField(max_length=10, null=True, blank=True)
    authorized_person = models.CharField(max_length=50)
    contact_info_mail = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
