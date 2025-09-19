from django.shortcuts import render, redirect
from users.forms import UserLoginForm, SignUpForm
from django.contrib.auth.models import User
from users.models import Contact
import re
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    
    if(request.user.is_authenticated):
            return redirect('home')
        
    if request.method == 'POST':
        
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(
                request,
                username=username,
                password=password
            )
                    
            if user is not None:
                auth.login(request, user)
                if user.is_authenticated:
                    return redirect('home')
                else:
                    messages.error(request, 'Erro ao autenticar o usuário.')
                    return render(request, 'users/login.html', {'form': form})
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
                return redirect('login')
           
        else:
            messages.error(request, 'Erro ao autenticar o usuário.')
            return render(request, 'users/signup.html', {'form': form})
            #check if passwords are the same
        
        
    form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def signup(request):
    
    if(request.user.is_authenticated):
        return redirect('home')
    
    if request.method == 'POST':
                        
        form = SignUpForm(request.POST)
    
        #check if form is valid
        if form.is_valid():
            
            fullName = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phoneNumber = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
            name_parts = fullName.strip().split()                 
            first_name = name_parts[0]
            last_name = " ".join(name_parts[1:]) 
             
            #forms.py already validate and return if there are errors   
            #if not form.errors:
            user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
            )
            user.save()
            user.contact.phone_number = phoneNumber
            user.contact.save()
            
            messages.success(request, 'Usuário criado com sucesso! Faça login para continuar.')
            return render(request, 'users/login.html', {'form': UserLoginForm(initial={'username': username})})
                   
        else:
            
            #if form is not valid
            messages.error(request, 'Não foi possível criar o usuário. Verifique os campos acima.')
            return render(request, 'users/signup.html', {'form': form})
            #check if passwords are the same
        
        
        
    else:
        form = SignUpForm()
            
    
    return render(request, 'users/signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')