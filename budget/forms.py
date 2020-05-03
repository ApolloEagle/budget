from django import forms

class ExpenseForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    ),
    amount = forms.DecimalField(
        max_digits=16,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "$500.00"
        })
    )