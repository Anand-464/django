from django.shortcuts import render
from .forms import LoginForm
def main(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        return render(request,'data.html',{
            'name' : form['name'].value,
            'email': form['email'].value,
            'age' : form['age'].value,
            'address' : form['address'].value
        })
    return render(request,'intro.html')