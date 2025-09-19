from django import forms
from django.contrib.auth.models import User
from users.models import Contact
import re

class UserLoginForm(forms.Form):
            
    username=forms.CharField(
        label='Nome de Usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joao.silva',
            }
        )
    )
    password=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    
class SignUpForm(forms.Form):
    full_name=forms.CharField(
        label='Nome Completo', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    
    username=forms.CharField(
        label='Nome de usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joao.silva',
            }
        )
    )
    
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    
    
    phone_number = forms.CharField(
        label='Telefone',
        required=True,
        max_length=15,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "(99)99999-9999",
            "oninput": "formatarTelefone(this)",
        })
    )
    
    password=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
     
    confirm_password=forms.CharField(
        label='Confirme sua Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )
    
    
    def clean_full_name(self):
        fullName = self.cleaned_data.get('full_name').strip()
        if fullName == '':
            raise forms.ValidationError('Este campo é obrigatório.')
            
        name_parts = fullName.split()
            
        if len(name_parts) < 2:
            raise forms.ValidationError('Por favor, insira seu nome completo.')
        return fullName
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number', '').strip()
        
        phone_only_numbers = re.sub(r"\D", "", phone_number)
        if len(phone_only_numbers) not in (10, 11):
            raise forms.ValidationError('Digite um número válido com DDD.')
        return phone_number
        
    def clean_username(self):
        username = self.cleaned_data.get('username').strip()
        
        if not username:
            raise forms.ValidationError('Este campo é obrigatório.')
        if " " in username:
            raise forms.ValidationError('Não é possível inserir espaços no nome de usuário.')
        
        #check if username already exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('username', 'Nome de usuário já existe!')
        return username  
        
    def clean_email(self):
        email = self.cleaned_data.get('email').strip()
        # check if email is valid
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso!')
        elif '@' not in email or '.' not in email.split('@')[-1]:
            raise forms.ValidationError('Por favor, insira um email válido.')
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password == '':
            raise forms.ValidationError('Este campo é obrigatório.')
        return password
        
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        #check if passwords are the same
        if password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem! Tente novamente.')
        return confirm_password
                  