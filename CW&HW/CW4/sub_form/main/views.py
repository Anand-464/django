from django.shortcuts import render
def msg(request):
    if request.GET:
        name = request.GET.get('name')
        return render(request,'result.html',{
            'formData':request.GET,
            'name': name
        })
    return render(request,'user.html' )