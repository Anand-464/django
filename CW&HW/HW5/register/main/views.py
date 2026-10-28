from django.shortcuts import render
from .forms import LoginForm
def result(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'msg.html',{
                 'email': form['email'].value
             })
    else:
        form = LoginForm()
    return render(request,'registration.html',{'form':form})