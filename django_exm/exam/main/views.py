from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .models import Weight_enter
from .forms import WeightForm
from django.utils import timezone
from django.contrib import messages


def home(request):
    return render(request, 'home.html')
 
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    context = {
        'user': request.user
    }
    return render(request, 'logout.html', context)



@login_required
def add_weight(request):
    if request.method == 'POST':
        form = WeightForm(request.POST)
        if form.is_valid():
            today = timezone.localdate()
            already_added = Weight_enter.objects.filter(
                user=request.user.username,
                date__date= today
            ).exists()
            if already_added:
                messages.error(
                    request,
                    "You have already added your weight today!"
                )
            else:
                weight_record = form.save(commit=False)
                weight_record.user = request.user.username
                weight_record.save()
                messages.success(
                    request,
                    "Weight added successfully!"
                )
                return redirect('weight_list')
    else:
        form = WeightForm()
    return render(
        request,
        'add_weight.html',
        {'form': form}
    )

@login_required
def weight_list(request):
    weights = Weight_enter.objects.filter(
        user=request.user.username
    ).order_by('date')
    paginator = Paginator(weights, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'weight_list.html', {
        'page_obj': page_obj
    })


@login_required
def weight_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    records = Weight_enter.objects.none()
    weight_loss = None
    error = None
    if start_date and end_date:
        try:
            start = timezone.datetime.strptime(
                start_date, '%Y-%m-%d'
            ).date()
            end = timezone.datetime.strptime(
                end_date, '%Y-%m-%d'
            ).date()
            if start > end:
                error = 'Start date must be before end date.'
            elif end > timezone.localdate():
                error = 'End date cannot be in the future.'
            else:
                records = Weight_enter.objects.filter(
                    user=request.user.username,
                    date__date__range=(start, end)
                ).order_by('date')
                if records.count() >= 2:
                    first_weight = records.first().weight
                    last_weight = records.last().weight
                    weight_loss = first_weight - last_weight
                elif records.count() == 1:
                    weight_loss = 0
        except ValueError:
            error = 'Please select valid dates.'
    return render(request, 'weight_report.html', {
        'records': records,
        'weight_loss': weight_loss,
        'start_date': start_date,
        'end_date': end_date,
        'error': error
    })



@login_required
def edit_weight(request, pk):
    weight_record = get_object_or_404(
        Weight_enter,
        id=pk,
        user=request.user.username
    )
    if request.method == 'POST':
        form = WeightForm(request.POST, instance=weight_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Weight updated successfully.')
            return redirect('weight_list')
    else:
        form = WeightForm(instance=weight_record)
    return render(request, 'edit_weight.html', {
        'form': form
    })



@login_required
def delete_weight(request, pk):
    weight_record = get_object_or_404(
        Weight_enter,
        id=pk,
        user=request.user.username
    )
    if request.method == 'POST':
        weight_record.delete()
        messages.success(request, 'Weight deleted successfully.')
        return redirect('weight_list')
    return render(request, 'delete_weight.html', {
        'weight_record': weight_record
    })