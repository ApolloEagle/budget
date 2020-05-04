from django.shortcuts import render
from budget.models import Expense
from .forms import ExpenseForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum

def budget_view(request):
    expenses = Expense.objects.all()
    total = Expense.objects.aggregate(total=Sum('amount'))['total']

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
        "expenses": expenses,
        "total": total,
    }
    
    return render(request, "budget_view.html", context)