from django.shortcuts import render
from .forms import Contact
from .models import User
def result(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            pers = User()
            pers.name = form.cleaned_data['name']
            pers.email = form.cleaned_data['email']
            pers.phonenumber = form.cleaned_data['phonenumber']
            pers.save()
            return render(request, 'result.html', {
                'message': 'Thank you user ' + form['name'].value()
            })
    else:
        form = Contact()
    return render(request,'info.html',{'form':form})