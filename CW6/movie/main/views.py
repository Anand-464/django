from django.shortcuts import render
from .forms import Entermovie
from .models import Movies
def result(request):
    if request.method == 'POST':
        form = Entermovie(request.POST)
        if form.is_valid():
            mov = Movies()
            mov.name = form.cleaned_data['name']
            mov.year = form.cleaned_data['year']
            mov.save()
            return render(request,'msg.html',{
                'name': form['name'].value,
                'year': form['year'].value
            })
    else:
        form = Entermovie()
    return render(request,'first.html',{'form':form})