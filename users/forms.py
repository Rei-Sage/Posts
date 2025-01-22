from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class LoginUser(forms.Form):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white ',
            'placeholder': 'Введите логин'
})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите пароль'
            }),
            validators=[validate_password]
    )
    
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        
        if len(password)<6:
            raise forms.ValidationError("Пароли не должен быть меньше 6")
        
        return password

from django.core.exceptions import ValidationError
import re

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите email'
        })
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите имя пользователя'
        })
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите пароль'
        }),
        validators=[validate_password]
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Повторите пароль'
        })
    )
    first_name = forms.CharField(
        label="Имя",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите настоящее имя'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите фамилию'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']
    def clean_new_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password2 != password1:
            raise forms.ValidationError("Пароли не совпадают.")
        
        return password2



class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите старый пароль'
        })
    )
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите новый пароль',
        }),
        validators=[validate_password]
    )
    new_password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Повторите новый пароль'
        })
    )
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
    
    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")
        
        if new_password1 != new_password2:
            raise forms.ValidationError("Пароли не совпадают.")
        
        return new_password2


# class ChangeProfile(forms.Form):
#     username = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
#             'placeholder': 'Введите имя '
#         })
#     )
#     email = forms.EmailField(
#         required=True,
#         label="Email",
#         widget=forms.EmailInput(attrs={
#             'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
#             'placeholder': 'Введите email'
#         })
#     )
#     first_name = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
#             'placeholder': 'Введите настоящее имя'
#         })
#     )
#     last_name = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] bg-[#3B3B3B] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
#             'placeholder': 'Введите фамилию'
#         })
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name']  

from django import forms

class ChangeProfile(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите имя'
        })
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите email'
        })
    )
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите настоящее имя'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-[#3B3B3B] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 pl-[40px] border-[#A259FF] hover:bg-gray-700 transition-colors border-[1px] border-solid rounded-[28px] text-white',
            'placeholder': 'Введите фамилию'
        })
    )
    # image = forms.ImageField(required=False)



    