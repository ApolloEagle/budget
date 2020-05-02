from django.db import models

class Expense(models.Model):
    name = models.TextField(max_length=255)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
