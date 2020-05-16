from django import forms
from django.core.exceptions import ValidationError

class ExpenseForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Expense Name"
        })
    )
    amount = forms.DecimalField(
        max_digits=16,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "$400.00"
        })
    )

class IncomeForm(forms.Form):
    income = forms.DecimalField(
        max_digits=16,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "$1000.00"
        })
    )
