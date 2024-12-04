from django.core.exceptions import ValidationError


def validate_telephone(value):
    if len(str(value)) < 11:
        raise ValidationError('Телефон не может быть меньше 11 символов')


def password_validator(value):
    if len(value) < 3:
        raise ValidationError('Пароль не может быть меньше 3 символов')

    if not any(char.isdigit() for char in value):
        raise ValidationError('Пароль должен содеражать хотябы одну цифру')


def driver_license_number_validator(value):
    if not len(str(value)) == 4:
        raise ValidationError('Номер лицензии должен состоять из 4 цифр')


def driver_license_series_validator(value):
    if not len(str(value)) == 6:
        raise ValidationError('Серия лицензии должна состоять из 6 цифр')
