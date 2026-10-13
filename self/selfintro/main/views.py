from django.shortcuts import render
from .forms import dataform
from .models import Movies
def result(request):
    if request.method == 'POST':
        form = dataform(request.POST)
        if form.is_valid():
            mov = Movies()
            data = form.cleaned_data
            mov.name = data['name']
            mov.year = data['year']
            mov.genre = data['genre']
            mov.rating = data['rating']
            mov.save()
            return render(request,'data.html',{
                'message':'Data submitted'
            })
    else:
        form = dataform()
    return render(request,'intro.html',{'form':form})