from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_time_between_8_and_18


class Application(models.Model):
    status_choices = {
        'new': 'Новая',
        'completed': 'Выполненная'
    }

    master = models.ForeignKey(
        get_user_model(), related_name='master_applications',
        null=True, blank=False, on_delete=models.SET_NULL,
        verbose_name='Мастер'
    )

    user = models.ForeignKey(
        get_user_model(), related_name='user_applications',
        blank=True, on_delete=models.CASCADE
    )

    status = models.CharField(default='new', max_length=50, choices=status_choices)
    date = models.DateTimeField('Дата', unique=True, validators=[validate_time_between_8_and_18])

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка мастера {self.master}, дата: {self.date}'