from django.shortcuts import render
from .models import Student, Courss


def index(request):
    return render(request, 'index.html')


def save_student(request):
    sno = request.POST['sno']
    sname = request.POST['sname']
    loc = request.POST['loc']
    s = Student(sno, sname, loc)
    s.save()
    return render(request, 'index.html')


def new_student(request):
    return render(request, 'newstudent.html')

