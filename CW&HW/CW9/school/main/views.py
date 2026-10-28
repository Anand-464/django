from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request, name):
    results = {
        'Abi': 85,
        'Eby': 92,
        'Abhi': 78
    }
    marks = results.get(name)
    return render(request, 'result.html', {
        'name': name,
        'marks': marks
    })
