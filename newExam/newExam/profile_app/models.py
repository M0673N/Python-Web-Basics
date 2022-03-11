from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from newExam.profile_app.validators import only_letters_validator, file_size


class Profile(models.Model):
    first_name = models.CharField(max_length=15, validators=[MinLengthValidator(2), only_letters_validator])
    last_name = models.CharField(max_length=15, validators=[MinLengthValidator(2), only_letters_validator])
    budget = models.FloatField(default=0, validators=[MinValueValidator(0)])
    profile_image = models.ImageField(blank=True, null=True, upload_to='images/', validators=[file_size])
