from django.shortcuts import render, get_object_or_404, redirect
from decimal import *

from .models import Account
from .forms import JournalEntryForm, CommentForm

def accounting_index(request, message=""):
    account_list = Account.objects.all()

    if request.method == "POST":
        acct_debits = Decimal(0.00)
        acct_credits = Decimal(0.00)

        try:
            account_name = request.POST.get('account_name')
            account_name2 = request.POST.get('account_name2')
        except:
            account_name = ""
            account_name2= ""

        try:
            amount = Decimal(request.POST.get('amount'))
            amount2 = Decimal(request.POST.get('amount2'))
        except:
            amount = Decimal(0.00)
            amount2 = Decimal(0.00)

        accounting_side = request.POST.get('accounting_side')
        accounting_side2 = request.POST.get('accounting_side2')

        found = False
        for account in account_list:
            if account.account_name == account_name:
                account_number1 = account.account_number
                found = True

        found2 = False
        for account in account_list:
            if account.account_name == account_name2:
                account_number2 = account.account_number
                found2 = True
       
        if accounting_side == "Debit":
            acct_debits += amount
        if accounting_side == "Credit":
            acct_credits += amount

        if accounting_side2 == "Debit":
            acct_debits += amount2
        if accounting_side2 == "Credit":
            acct_credits += amount2

        if amount <= 0 or amount2 <= 0:
            message = "Cannot create a zero dollar entry"

        if acct_credits != acct_debits:
            message = "Debits and Credits don't balance." + " Credits - " + str(acct_credits) + " Debits - " + str(acct_debits)

        if found2 == False or found == False:
            message = "One or both of those accounts don't exist"
        
        #approval
        if acct_credits == acct_debits and acct_credits > 0 and acct_debits > 0 and found == True and found2 == True:
            acct1 = Account.objects.get(account_number=account_number1)
            acct2 = Account.objects.get(account_number=account_number2)

            print(acct1.account_type)
            print(acct2.account_type)

            #account one
            if acct1.account_type == "A" and accounting_side == "Credit":
                amount = amount *-1
                print(amount)

            if acct1.account_type == "L" and accounting_side == "Debit":
                amount = amount *-1
                print(amount)

            if acct1.account_type == "E" and accounting_side == "Debit":
                amount = amount *-1
                print(amount)

            #account two
            if acct2.account_type == "A" and accounting_side2 == "Credit":
                amount2 = amount2 *-1
                print(amount)

            if acct2.account_type == "L" and accounting_side2 == "Debit":
                amount2 = amount2 *-1
                print(amount)

            if acct2.account_type == "E" and accounting_side2 == "Debit":
                amount2 = amount2 *-1
                print(amount)

            #set new balances
            acct1.account_balance = acct1.account_balance + amount
            acct2.account_balance = acct2.account_balance + amount2

            #save to db
            acct1.save()
            acct2.save()

            message = "Entry approved"
            account_list = Account.objects.all()
            context = {
                'account_list': account_list,
                'message': message,
            }
            
            return render(request, 'accounting/index.html', context)

        # try:
        #     print(account_number1)
        # except:
        #     print("that account does not exist")
        # print(account_name)
        
        # try:
        #     print(account_number2)
        # except:
        #     print("that account does not exist")
        # print(account_name2)

        # print(amount)
        # print(amount2)
        # print(accounting_side)
        # print(accounting_side2)
        # print(acct_debits)
        # print(acct_credits)


    context = {
        'account_list': account_list,
        'message': message,
    }

    return render(request, 'accounting/index.html', context)

def account_delete_view(request, id):
    obj = get_object_or_404(Account, id=id)

    if request.method == "POST":
        obj.delete()

    return render(request, 'accounting/delete.html')

def journal_entry_view(request):
    form = JournalEntryForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'accounting/journal_entry.html', context)


def custom_view(request):
    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'accounting/journal_entry.html', context)