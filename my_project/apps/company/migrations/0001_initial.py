# Generated by Django 4.2.7 on 2023-11-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                (
                    'tax_number',
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ('authorized_person', models.CharField(max_length=50)),
                (
                    'contact_info_mail',
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
            ],
        ),
    ]
