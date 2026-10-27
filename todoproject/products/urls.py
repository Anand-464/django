from . import views
from django.urls import path

urlpatterns = [
        path('create/',views.product_create,name='createproduct'),
        path('retrieve/', views.product_read, name='retrieveproduct'),
        path('update/<int:id>/', views.product_update, name='updateproduct'),
        path('delete/<int:pk>/', views.product_delete, name= 'deleteproduct'),
        path('listing/', views.listing, name= 'page_list'),
        path('<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
        path('send_product_email/<int:pk>/', views.send_product_email, name='send_product_email'),
    ]