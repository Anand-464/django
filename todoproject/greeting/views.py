from django.shortcuts import render
from .forms import LoginModelForm
from .models import Customer

def greeting(request):
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'form-data.html',{
                'message': 'Data saved to db',
                'customer': cust
            })
    else:
        form = LoginModelForm()
    return render(request,'index.html',{'form':form})

def greeting2(request):
    data = Customer.objects.all()
    cust = Customer.objects.get(pk=1)
    return render(request,'index2.html',{
        'data':data,
        'list': cust
    })