from django.urls import path
from . import views
urlpatterns = [
    path('homeapi',views.homeapi,name='home_api'),
    path('signup',views.signup,name='signup_api'),
    path('login', views.login, name= 'login_api')
]