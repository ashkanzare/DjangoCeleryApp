from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Fibonacci
from .tasks import calc_fib


def calc_fib_view(request):

    last_members = Fibonacci.objects.all()
    print(last_members)
    return HttpResponse('ok')