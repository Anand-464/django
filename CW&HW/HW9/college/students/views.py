from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def student_list(request, message):
    students = ['Arun', 'Anu', 'Rahul']

    return render(request, 'student_list.html', {
        'students': students,
        'message': message
    })