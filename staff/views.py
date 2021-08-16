from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    employees = Employee.objects.all()
    dict_obj = {'employees': employees}
    return render(request, 'staff/index.html', dict_obj)


def staff_detail(requet, id):
    employee = Employee.objects.filter(id=id)
    employees = Employee.objects.filter(~Q(id=id))
    dict_obj = {'employee': employee, 'employees': employees}
    return  render(requet, 'staff/emplyee_profile.html', dict_obj)
