from django.core.exceptions import ValidationError
from datetime import time


def validate_time_between_8_and_18(value):
    event_time = value.time()
    start_time = time(8, 0)
    end_time = time(18, 0)

    if not (start_time <= event_time <= end_time):
        raise ValidationError('Время должно быть между 08:00 и 18:00.')
