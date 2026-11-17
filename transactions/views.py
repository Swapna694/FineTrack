
from django.shortcuts import render

def home(request):
    return render(request, 'transactions/home.html')


# Create your views here.
