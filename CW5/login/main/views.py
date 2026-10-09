from django.shortcuts import render
from .forms import LoginForm
def msg(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'result.html',{
                 'email': form['email'].value
             })
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})