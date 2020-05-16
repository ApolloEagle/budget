from django.db import models
from django.forms import ModelForm

class Expense(models.Model):
    name = models.TextField(max_length=255)
    amount = models.DecimalField(max_digits=16, decimal_places=2)

class Income(models.Model):
    income = models.DecimalField(max_digits=16, decimal_places=2)

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount']

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['income']