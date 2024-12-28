from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget, Transaction

# Create your views here.

def index(request):
    budgets = Budget.objects.all()
    return render(request, 'index.html', {'budgets' : budgets})

def add_budget(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        Budget.objects.create(name=name, amount=amount)
        return redirect('index')
    
    return render(request, 'add_budget.html')

def delete_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    
    if request.method == 'POST':
        budget.delete()
        return redirect('index')
    
    return redirect('index')

def add_transaction(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    if request.method == 'POST':
        description = request.POST.get("description")
        amount = request.POST.get('amount')

        Transaction.objects.create(budget=budget,description=description, amount=amount)
        return redirect('view_transactions', budget_id=budget.id)
    
    return render(request, 'add_transaction.html', {"budget" : budget})

def view_transactions(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    transactions = Transaction.objects.filter(budget=budget)
    return render(request, 'view_transactions.html', {'transactions' : transactions, 'budget' : budget})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('view_transactions', budget_id=transaction.budget.id)

    return redirect('view_transactions.html', budget_id=transaction.budget.id)