from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_read, name='home'),
    path('add/', views.add_product, name='add_product'),
    path('pdf/<int:pk>/', views.generate_pdf, name='generate_pdf'),
    path('email/<int:pk>/', views.send_product_email, name='send_product_email'),
]