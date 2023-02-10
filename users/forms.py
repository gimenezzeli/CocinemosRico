from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import UserProfile
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True,label="Usuario")
    email = forms.EmailField(label="Email")    
    first_name= forms.CharField(label='Nombre')
    last_name= forms.CharField(label='Apellido')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['username','first_name','last_name','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UserUpdateForm(forms.ModelForm):
    username= forms.CharField(label='Nombre de usuario')
    first_name= forms.CharField(label='Nombre')
    last_name= forms.CharField(label='Apellido')
    phone= forms.CharField(max_length=25, label='Telefono')
    birt_date= forms.DateField(label='Fecha de nacimiento')
    profile_picture= forms.ImageField(label='Foto de perfil')
    class Meta:
        model= UserProfile
        fields=['username','first_name','last_name','phone', 'profile_picture']
