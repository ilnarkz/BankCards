import random
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from django.urls import reverse
from django.utils import timezone

STATUS_CHOICES = [
    ('Активирована', 'Активирована'),
    ('Деактивирована', 'Деактивирована'),
    ('Просрочена', 'Просрочена'),
]


HOW_LONG_CHOICES = [
    ('1', '1 месяц'),
    ('6', '6 месяцев'),
    ('12', '1 год')
]


def get_card_series():
    num = random.randint(1, 10000)
    return num


def get_card_number():
    num = random.randint(1, 1000000000000)
    return num


class Card(models.Model):
    card_series = models.IntegerField(default=get_card_series)
    card_number = models.BigIntegerField(default=get_card_number)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='Активирована')
    created_at = models.DateTimeField(default=timezone.now)
    how_long = models.CharField(max_length=16, choices=HOW_LONG_CHOICES, default='1')
    amount = models.FloatField(default=1000.00)

    def get_absolute_url(self):
        return reverse('cards:card_list')

    def get_end_date(self):
        delta = int(self.how_long)
        date = self.created_at + relativedelta(months=delta)
        return date.strftime('%d.%m.%Y %H:%M')

    def is_expired(self, *args, **kwargs):
        delta = int(self.how_long)
        date = self.created_at + relativedelta(months=delta)
        if datetime.today().timestamp() > date.timestamp():
            self.status = 'Просрочена'
            super().save(*args, **kwargs)
