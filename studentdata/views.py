from django.shortcuts import render, HttpResponseRedirect
from .forms import Studentregistration
from .models import User

# Create your views here.

#This function will add and delete the student data
def addandshow(request):
    if request.method == 'POST':
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return render(request, 'studentdata/success.html')
    else:
        fm = Studentregistration()
    stud = User.objects.all()
    return render(request, 'studentdata/addandshow.html', {'form':fm , 'stu':stud})

#This function will delete the data
def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    if request.method == 'POST':
        PI = User.objects.get(pk=id)
        fm = Studentregistration(request.POST, instance=PI)
        if fm.is_valid():
            fm.save()
    else:
        PI = User.objects.get(pk=id)
        fm = Studentregistration(instance=PI)

    return render(request, 'studentdata/update.html', {'form':fm})