from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_home, name='student_home'),
    path('list/', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('edit/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('search/', views.student_search, name='student_search'),
]
