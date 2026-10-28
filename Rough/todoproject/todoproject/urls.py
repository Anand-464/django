"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from greeting import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.greeting, name='home'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('page/<str:title>/', views.pages, name='page'),
    path('count/<int:num>/', views.count, name='count'),
    path('contactus/', include('contactus.urls')),
    path('products/', include('products.urls')),
    path('pagevisit/', views.pagevisit, name='page_visit'),
    path('signup/', views.signup_page, name= 'signup'),
    path('login/', views.login_page, name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('productsapi/', include('productsapi.urls')),
    path('fileupload/', include('filemaker.urls'))

]