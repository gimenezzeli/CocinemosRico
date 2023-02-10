from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import RegisterForm, UserUpdateForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



def LoginView(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context={
            'form': form,
        }
        return render(request, 'users/login.html', context=context)
    elif request.method == 'POST':
        form= AuthenticationForm(request=request, data= request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')

            user= authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context={
                    'message':f'Bienvenido {username}!!'
                }
                return render(request, 'index.html', context=context)

        form= AuthenticationForm()
        context={
            'form':form,
            'errors':'Usuario o contraseña incorrectos!',
        }
        return render(request, 'users/login.html', context=context)


def register(request):
    if request.method == 'GET':
        form= RegisterForm()
        context={
            'form': form,
        }
        return render(request, 'users/register.html', context=context)
    elif request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            user=form.save() #al hacer .save() se crea el usuario
            UserProfile.objects.create(user=user)
            return redirect('login')

        context={
            'errors':form.errors,
            'form':RegisterForm(),
        }
        
        return render(request, 'users/register.html', context=context)


@login_required
def update_user(request):
    user= request.user.profile
    if request.method == 'GET':
        form= UserUpdateForm(
            initial={
                'username':user.username,
                'first_name':user.first_name,
                'last_name':user.last_name,      
                'phone': user.phone,
                'birth_date': user.birth_date,
                'profile_picture': user.profile_picture,
            }
        )
        context={
            'form': form,
        }
        return render(request, 'users/update_profile.html', context=context)
    elif request.method == 'POST':
        form= UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user.username= form.cleaned_data.get('username')
            user.first_name= form.cleaned_data.get('first_name')
            user.last_name= form.cleaned_data.get('last_name')
            user.phone=form.cleaned_data.get('phone')
            user.birth_date= form.cleaned_data.get('birth_date')
            user.profile_picture=form.cleaned_data.get('profile_picture')
            user.save()
            return redirect('index')

        context={
            'errors':form.errors,
            'form':UserUpdateForm(),
        }
        
        return render(request, 'users/update_profile.html', context=context)

