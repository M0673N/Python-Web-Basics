from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from myMusicApp.profiles.validators import alphanum_and_underscore_validator


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), alphanum_and_underscore_validator])
    email = models.EmailField()
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
