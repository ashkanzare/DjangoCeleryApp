from celery import shared_task

from fib.models import Fibonacci


@shared_task
def calc_fib():
    print('salam')
    last_members = Fibonacci.objects.all().order_by('-pk')

    num_1, num_2 = last_members[0], last_members[1]
    new_num_1 = num_1.value + num_2.value
    index_1 = num_2.index + 1
    index_2 = index_1 + 1
    new_num_2 = new_num_1 + num_2.value

    Fibonacci.objects.create(index=index_1, value=new_num_1)
    Fibonacci.objects.create(index=index_2, value=new_num_2)
    print('fibL:', num_1, num_2)
    return new_num_1, new_num_2
