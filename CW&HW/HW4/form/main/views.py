from django.shortcuts import render

# Create your views here.
def msg(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     color = request.POST.get('color')
     return render(request,'form-data.html',{
         'formData':request.POST,
         'name': name,
         'color': color
     })
    return render(request,'form.html')