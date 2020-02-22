from django.shortcuts import render

from django.core.paginator import Paginator
from .models import Emp


def index(request):
    i = request.GET.get('page', 1)
    emps = Emp.objects.all()
    paginator = Paginator(emps, 5)
    page = paginator.page(i)

    return render(request, 'show.html', {'emp': page})

# Create your views here.
