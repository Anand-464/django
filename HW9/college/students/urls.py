from django.urls import path
from . import views
app_name = 'students'
urlpatterns = [
    path('<str:message>/', views.student_list, name='list'),
]