from . import views
from django.urls import path

urlpatterns = [
        path('create/',views.product_create,name='createproduct'),
        path('retrieve/', views.product_read, name='retrieveproduct'),
        path('update/<int:id>/', views.product_update, name='updateproduct'),
        path('delete/<int:pk>/', views.product_delete, name= 'deleteproduct'),
        path('listing/', views.listing, name= 'page_list'),
    ]