from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from news.models import *
from multiupload.fields import MultiFileField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'tags', 'image','location']
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-gray-100 placeholder-gray-400 transition-all duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent hover:bg-gray-75',
            'placeholder': 'Введите название'}),
            'location': forms.TextInput(attrs={
            'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-gray-100 placeholder-gray-400 transition-all duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent hover:bg-gray-75',
            'placeholder': 'Введите локацию'}),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 '
                        'text-gray-100 placeholder-gray-400 '
                        'transition-all duration-300 ease-in-out '
                        'focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent '
                        'hover:bg-gray-750 resize-none',
                'rows': 4,
                'placeholder': 'Опишите ваш пост'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 '
                        'text-gray-100 cursor-pointer '
                        'transition-all duration-300 ease-in-out '
                        'focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent '
                        'hover:bg-gray-750'
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'rounded-md bg-gray-800 border-gray-700 transition-all duration-200 ease-in-out focus:ring-2 focus:ring-offset-gray-900 hover:border-red-400'
            }),
            'image': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-400 '
                        'file:mr-4 file:py-2.5 file:px-6 '
                        'file:rounded-lg file:border-0 '
                        'file:text-sm file:font-semibold '
                        'file:bg-red-500 file:text-white '
                        'hover:file:bg-red-600 '
                        'transition-all duration-300 ease-in-out '
                        'cursor-pointer '
                        'focus:outline-none'
            }),
        }

# # class PostForm(forms.ModelForm):
# #     class Meta:
# #         model = Post
# #         exclude = ['creator',]
# #         # fields = ['name','category','price', 'highest_bid', 'image', 'minted_date']
# #         widgets = {
# #             'name': forms.TextInput(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'description': forms.Select(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'category': forms.Select(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'price': forms.NumberInput(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'highest_bid': forms.NumberInput(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'image': forms.FileInput(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'minted_date': forms.DateInput(attrs={
# #                 'type': 'date',
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #         }

# #     def save(self, commit=True, user=None):
# #         instance = super().save(commit=False)
# #         if not instance.creator and user:  # если создатель не был указан
# #             instance.creator = user  # устанавливаем текущего пользователя
# #         if commit:
# #             instance.save()
# #         return instance    


# #     def clean_price(self):
# #         price = self.cleaned_data.get('price')
# #         if price <= 0:
# #             raise forms.ValidationError("Цена не может быть отрицательной или нулевой.")
# #         return price

# #     def clean_highest_bid(self):
# #         highest_bid = self.cleaned_data.get('highest_bid')
# #         if highest_bid is not None and highest_bid <= 0:
# #             raise forms.ValidationError("Высшая ставка не может быть отрицательной или нулевой.")
# #         return highest_bid
    
# #     def form_valid(self, form):
# #         form.instance.creator = self.request.user  # Устанавливаем текущего пользователя
# #         return super().form_valid(form)

# # class InformationForm(forms.ModelForm):
# #     class Meta:
# #         model = Information
# #         fields = ['description', 'blockchain','tags']
# #         widgets = {
# #             'description': forms.Textarea(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'blockchain': forms.TextInput(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'etherscan_link': forms.URLInput(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'original_link': forms.URLInput(attrs={
# #                 'class': 'w-full bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #             'tags': forms.CheckboxSelectMultiple(attrs={
# #                 'class': 'bg-gray-700 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'
# #             }),
# #         }

# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.fields['tags'].queryset = Tag.objects.all()

# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите пароль'
#         })
#     )
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Повторите пароль'
#         })
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         if password != confirm_password:
#             raise forms.ValidationError("Пароли не совпадают")

#         email = cleaned_data.get('email')
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             raise forms.ValidationError("Введите правильный адрес электронной почты")

#         return cleaned_data
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Введите имя пользователя'
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Введите пароль'
#     }))