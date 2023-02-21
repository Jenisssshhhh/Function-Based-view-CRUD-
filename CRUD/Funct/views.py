from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import EmployeeRegistration
from .models import Employee

# Create your views here.
def home(request):
    if request.method == "POST":
        fm =EmployeeRegistration(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['name']
            e = fm.cleaned_data['email']
            p = fm.cleaned_data['password']
            user = Employee(name = n, email = e,password = p)
            user.save()
            fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()
    emp=Employee.objects.all()
    return render (request,'add.html',{'form':fm,'em':emp})




def delete(request,id):
    if request.method == 'POST':
        j = Employee.objects.get(pk=id)
        j.delete()
        return redirect('/')


def update(request,id):
    if request.method == "POST":
        k = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST,instance = k)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        k = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(instance = k)
    return render (request,'update.html',{'form':fm})

