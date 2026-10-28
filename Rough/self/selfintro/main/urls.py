from django.urls import path
from . import views

urlpatterns = [
    path('',views.result),
    path('second/',views.greeting),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.log_out, name= 'logout'),
    path('create/', views.create_mov, name= 'create'),
    path('read/', views.read_mov, name= 'read'),
    path('<int:pk>/update/', views.update_mov, name= 'update'),
    path('<int:pk>/delete/', views.delete_mov, name='delete')
]
