from django.shortcuts import render, redirect, get_object_or_404
from .forms import dataform
from .models import Movies
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import MovieSerializer


def result(request):
    if request.method == 'POST':
        form = dataform(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'data.html',{
                'message': 'Data saved to db',
                'customer': cust
            })
    else:
        form = dataform()
    return render(request,'intro.html',{'form':form})

def greeting(request):
    data = Movies.objects.all()
    return render(request,'data.html',{'data':data})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            return redirect('data')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required(login_url = '/login/')
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    context ={
        'user': request.user
    }
    return render (request, 'logout.html', context)


#create
@api_view(['POST'])
@permission_classes([AllowAny])
def create_mov(request):
    form= dataform(request.POST)
    if form.is_valid():
        movie = form.save()
        return Response({'id': movie.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

#read
@api_view(['GET'])
@permission_classes([AllowAny])
def read_mov(request):
    mov = Movies.objects.all()
    serializer= MovieSerializer(mov, many= True)
    return Response(serializer.data)

#update
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_mov(request, pk):
    movie= get_object_or_404(Movies, pk=pk)
    form= dataform(request.data, instance=movie)
    if form.is_valid():
        form.save()
        serializer= MovieSerializer(movie)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

#delete
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_mov(request, pk):
    try:
        movie= Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    movie.delete()
    return Response("deleted successfully")