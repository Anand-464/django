from django.urls import path
from . import views
urlpatterns = [
    path('create', views.create, name='create'),
    path('read', views.list, name= 'read'),
    path('<int:pk>/update', views.update, name= 'update'),
    path('<int:pk>/delete', views.delete, name= 'delete')
]