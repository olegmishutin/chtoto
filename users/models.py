from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import (
    validate_telephone, password_validator,
    driver_license_number_validator,
    driver_license_series_validator
)
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    date_joined = None
    email = None

    patronymic = models.CharField('отчество', max_length=150, null=True, blank=True)
    telephone = models.BigIntegerField('телефон', null=True, blank=True, validators=[validate_telephone])
    password = models.CharField('пароль', max_length=128, validators=[password_validator])

    driver_license_number = models.IntegerField(
        'номер вод. удостоверения', validators=[driver_license_number_validator])

    driver_license_series = models.IntegerField(
        'серия вод. удостоверения', validators=[driver_license_series_validator]
    )

    is_worker = models.BooleanField(default=False, blank=True)

    EMAIL_FIELD = ''
    REQUIRED_FIELDS = ['driver_license_number', 'driver_license_series']

    objects = CustomUserManager()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'.strip()
