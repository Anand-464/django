from django.shortcuts import render

# Create your views here.
def students(request):
    student_list = [
        {"name": "Anu", "grade": "A", "passed": True},
        {"name": "Rahul", "grade": "B", "passed": True},
        {"name": "Arun", "grade": "C", "passed": False},
        {"name": "Meera", "grade": "A+", "passed": True},
    ]

    return render(request, "students.html", {
        "students": student_list
    })