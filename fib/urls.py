from django.urls import path

from fib.views import calc_fib_view

urlpatterns = [
    path('', calc_fib_view, name='fibbo')
]