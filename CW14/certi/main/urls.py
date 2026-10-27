from . import views
from django.urls import path

urlpatterns = [
    path('', views.certificate_form, name='certificate_form'),
]