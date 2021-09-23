from django.contrib import admin

# Register your models here.
from fib.models import Fibonacci

admin.site.register(Fibonacci)