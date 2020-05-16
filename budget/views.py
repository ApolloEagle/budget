from django.shortcuts import render
from budget.models import Expense
from .forms import ExpenseForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum

def budget_view(request):
    expenses = Expense.objects.all()
    total = Expense.objects.aggregate(total=Sum('amount'))['total']

    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            if 'create-expense' in request.POST:
                expense = Expense(
                    name=form.cleaned_data["name"],
                    amount=form.cleaned_data["amount"]
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
        "form": form,
        "expenses": expenses,
        "total": total,
    }
    
    return render(request, "budget_view.html", context)