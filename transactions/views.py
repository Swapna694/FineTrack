from django.shortcuts import render,redirect,get_object_or_404
from .models import Transaction
from django.db.models import Sum
from .forms import TransactionForm



def home(request):

    transactions = Transaction.objects.all().order_by('-date')

    total_income = Transaction.objects.filter(
        transaction_type='Income'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    total_expenses = Transaction.objects.filter(
        transaction_type='Expense'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expenses

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance
    }

    return render(request, 'transactions/home.html', context)


def add_transaction(request):

    if request.method == 'POST':

        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TransactionForm()

    return render(request, 'transactions/add_transaction.html', {
        'form': form
    })


def edit_transaction(request, id):

    transaction = get_object_or_404(Transaction, id=id)

    if request.method == 'POST':

        form = TransactionForm(request.POST, instance=transaction)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'transactions/edit_transaction.html', {
        'form': form,
        'transaction': transaction
    })


def delete_transaction(request, id):

    transaction = get_object_or_404(Transaction, id=id)

    if request.method == 'POST':
        transaction.delete()
        return redirect('home')

    return render(request, 'transactions/delete_transaction.html', {
        'transaction': transaction
    })