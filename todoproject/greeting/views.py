from django.shortcuts import render
from .forms import LoginForm
def greeting(request):
    if request.method == 'POST':
     form = LoginForm(request.POST)
     return render(request,'form-data.html',{
         'email': form['email'].value,
         'password': form['password'].value
        })
    return render(request,'index.html')