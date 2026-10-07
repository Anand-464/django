from django.shortcuts import render

# Create your views here.
def employees(request):
    employee_list = [
        {
            "name": "Anu",
            "job_title": "Web Developer",
            "salary": 30000,
            "full_time": True
        },
        {
            "name": "Rahul",
            "job_title": "Designer",
            "salary": 25000,
            "full_time": False
        },
        {
            "name": "Meera",
            "job_title": "Manager",
            "salary": 50000,
            "full_time": True
        },
        {
            "name": "Arun",
            "job_title": "Tester",
            "salary": 28000,
            "full_time": False
        }
    ]
    return render(request, "employees.html", {
        "employees": employee_list
    })