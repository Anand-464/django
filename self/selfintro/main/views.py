from django.shortcuts import render
from .forms import dataform
from .models import Movies

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
