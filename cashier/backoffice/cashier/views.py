from django.shortcuts import render

# Create your views here.


def CashierView(request):
    context = {}
    return render(request, 'backoffice/cashier/index.html', context)
