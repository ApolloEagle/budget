from django.shortcuts import render
from budget.models import Expense
from .forms import ExpenseForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def budget_view(request):
    expenses = Expense.objects.all()

    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = Expense(
                name=form.cleaned_data["name"],
                amount=form.cleaned_data["amount"]
            )
            expense.save()

            return HttpResponseRedirect('/')

    context = {
        "form": form,
        "expenses": expenses
    }
    
    return render(request, "budget_view.html", context)