from django.shortcuts import render, redirect
from .forms import dataform
from .models import Movies
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def result(request):
    if request.method == 'POST':
        form = dataform(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'data.html',{
                'message': 'Data saved to db',
                'customer': cust
            })
    else:
        form = dataform()
    return render(request,'intro.html',{'form':form})

def greeting(request):
    data = Movies.objects.all()
    return render(request,'data.html',{'data':data})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            return redirect('data')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required(login_url = '/login/')
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    context ={
        'user': request.user
    }
    return render (request, 'logout.html', context)