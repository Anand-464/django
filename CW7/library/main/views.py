from django.shortcuts import render
from .forms import LibraryModelForm
from .models import book

def out(request):
    if request.method == 'POST':
        form = LibraryModelForm(request.POST)
        if form.is_valid():
            per = form.save()
            return render(request,'output1.html',{
                'message': 'Data saved to db',
                })
    else:
        form = LibraryModelForm()
    return render(request,'input.html',{'form':form})

def greeting(request):
    data = book.objects.all()
    return render(request,'output2.html',{'data':data})