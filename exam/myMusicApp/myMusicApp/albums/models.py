from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'),
                                                     ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'),
                                                     ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'),
                                                     ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')])
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0)])
