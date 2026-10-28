from django.shortcuts import render, redirect
from .forms import LoginModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


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

@login_required(login_url= '/login/')
def aboutUs(request):
    return render(request,'about-us.html')

def pages(request, title):
    return render(request,'pages.html',{'title':title})

def count(request, num):
    return render(request,'count.html',{'num': num})

def pagevisit(request):
    count = request.session.get('page_count',0)
    count +=1
    request.session['page_count']= count
    return render(request, 'page_view.html',{'count': count})

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createproduct')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)


def user_check(user):
    return user.username.endswith('@example.com')

@login_required(login_url='/login/')
@user_passes_test(user_check,login_url='/login/')
def aboutUs(request):
    return render(request,'about-us.html')