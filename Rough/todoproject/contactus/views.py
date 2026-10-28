from django.shortcuts import render

def contactus(request):
    return render(request,'contactus/contact-us.html')

def contactusform(request):
    return render(request,'contactus/contact-us-form.html')