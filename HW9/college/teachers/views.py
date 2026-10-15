from django.shortcuts import render

def teacher_list(request, message):
    teachers = ['John', 'Mary', 'Anjali']

    return render(request, 'teacher_list.html', {
        'teachers': teachers,
        'message': message
    })