from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=30)
    expense_image = models.URLField()
    description = models.TextField(blank=True)
    price = models.FloatField()
