from django.core.exceptions import ValidationError
from django.db import models


def min_value_validator(value):
    if value < 0:
        raise ValidationError('Make sure the pages are a positive number!')


class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(validators=[min_value_validator])
    description = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=20)
