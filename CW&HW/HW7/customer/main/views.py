from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
def add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'msg.html',{
                'message': 'Data saved to db'            })
    else:
        form = CustomerForm()
    return render(request,'first1.html',{'form':form})

def all(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'disp1.html', {'customers': customers})

def filtered(request):
    customers = Customer.objects.filter(email__endswith='@example.com').order_by('name')
    return render(request, 'disp2.html', {'customers': customers})