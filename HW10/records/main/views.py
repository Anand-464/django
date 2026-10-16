from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Student
from .forms import  StudentForm

def student_home(request):
    query = request.GET.get('search', '').strip()
    student_list = Student.objects.all()
    if query:
        student_list = student_list.filter(name__icontains=query)

    return render(request, 'home.html', {
        'student_list': student_list,
        'query': query,
    })
    
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_home')
    else:
        form = StudentForm()
    return render(request, 'create.html', {'form': form, 'title': 'Add Student'})

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update.html', {'form': form})

def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_home')
    
    return render(request, 'delete.html', {'student': student})

def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students, 5)
    student_page = request.GET.get('page')
    student_obj = paginator.get_page(student_page)
    
    return render(request, 'list.html', {'student_obj': student_obj})

def student_search(request):
    query = request.GET.get('search', '')
    students = Student.objects.filter(name__icontains=query)

    return render(request, 'student_list.html', {'students': students, 'query': query})