from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def welcome(request):
    count = request.session.get('visit_count', 0)
    count += 1
    request.session['visit_count'] = count

    return render(request, 'welcome.html', {'count': count})


@login_required(login_url='/login/')
def user_logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')

    return render(request, 'logout.html')
