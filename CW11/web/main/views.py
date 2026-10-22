from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('visit')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def user_logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)

@login_required(login_url='/login/')
def pagevisit(request):
    count = request.session.get('page_count', 0)
    count += 1
    request.session['page_count'] = count
    
    return render(request,'visited.html', {'count': count})