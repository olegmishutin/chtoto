# Generated by Django 5.1.3 on 2024-12-03 18:41

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='driver_license_series',
            field=models.PositiveSmallIntegerField(validators=[users.validators.driver_license_series_validator], verbose_name='серия вод. удостоверения'),
        ),
    ]
