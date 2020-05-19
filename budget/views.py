from django.shortcuts import render
from budget.models import Expense, Income
from .forms import ExpenseForm, IncomeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum

# Check email

def budget_view(request):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()
    incTotal = Income.objects.aggregate(total=Sum('income'))['total']
    expTotal = Expense.objects.aggregate(total=Sum('amount'))['total']

    expForm = ExpenseForm()
    incForm = IncomeForm()
    if request.method == 'POST':
        expForm = ExpenseForm(request.POST)
        incForm = IncomeForm(request.POST)
        if incForm.is_valid():
            if 'create-expense' in request.POST:
                income = Income(
                    income=incForm.cleaned_data["income"],
                )

                income.save()

                return HttpResponseRedirect('/')
        
            elif 'edit-income' in request.POST:

                return HttpResponseRedirect('/')

            else:
                income = Income.objects.get(id=request.POST.get("delete-income"))
                income.delete()
                
                return HttpResponseRedirect('/') 

        if expForm.is_valid():
            if 'create-expense' in request.POST:
                expense = Expense(
                    name=expForm.cleaned_data["name"],
                    amount=expForm.cleaned_data["amount"]
                )

                expense.save()

                return HttpResponseRedirect('/')
        
            elif 'edit-expense' in request.POST:

                return HttpResponseRedirect('/')

            else:
                expense = Expense.objects.get(id=request.POST.get("delete-expense"))
                expense.delete()
                
                return HttpResponseRedirect('/') 

    context = {
        "incForm": incForm,
        "expForm": expForm,
        "incomes": incomes,
        "expenses": expenses,
        "incTotal": incTotal,
        "expTotal": expTotal,
    }
    
    return render(request, "budget_view.html", context)