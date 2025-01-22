from django.shortcuts import render, redirect
from news.models import *
from .forms import LoginUser
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)  
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('/')  
            else:
                messages.error(request, 'Не верно пароль или логин')
        # else:
        #     for field, errors in form.errors.items():
        #         for error in errors:
        #             messages.error(request, f"Ошибка в  {field}: {error}")
    else:
        form = LoginUser()

    return render(request, 'login.html', {'form': form})



def user_logout(request):
    logout(request)  
    return redirect('/')



# from .forms import RegistrationForm



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            # messages.success(request, 'Аккаунт создан!')
            return redirect('/')  
        # else:
        #     messages.error(request, 'Ошибка в форме.')
    else:
        form = RegistrationForm()
    
    return render(request, 'user/register.html', {'form': form})


from django.contrib.auth.decorators import login_required
@login_required
def change_password(request):
    if request.method == 'POST':
        form =CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Пароль изменен!')
            return redirect('/profil')  
        # else:
            # messages.error(request, 'ошибки в форме')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'user/change_password.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404



# # @login_required
# # def change_profile(request):
# #     if request.method == 'POST':
# #         form = ChangeProfile(request.POST, instance=request.user)  
# #         if form.is_valid():
# #             form.save() 
# #             messages.success(request, 'Изменен')
# #             return redirect('/')
# #         else:
# #             for field, errors in form.errors.items():
# #                 for error in errors:
# #                     messages.error(request, f"Error in {field}: {error}")
# #     else:
# #         form = ChangeProfile(instance=request.user)  

# #     return render(request, 'change_profile.html', {'form': form})
def get_artist_image(user):
    try:
        img = Avatar.objects.get(user=user)
        return img if img.image else None
    except Avatar.DoesNotExist:
        return None

@login_required
def change_profile(request):
    img = get_artist_image(request.user)
    if request.method == 'POST':
        form = ChangeProfile(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            user.username = cd['username']
            user.email = cd['email']
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            update_session_auth_hash(request, user) 
            # messages.success(request, 'Код 016 (Успешно)')
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Код 02 {field}: {error}")
    else:
        form = ChangeProfile(initial={
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        })
    context={
        'form':form,
        'item':img
    }
    return render(request, 'user/change_profile.html', context)

@login_required
def change_image(request):
    img = get_object_or_404(Avatar, user=request.user)

    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        if uploaded_file:
            img.image = uploaded_file
            img.save()
            # messages.success(request, 'Фото успешно обновлено.')
            return redirect('change_profile/')  
        else:
            messages.error(request, 'Пожалуйста, выберите изображение.')
    context = {
        'img': img
    }
    return render(request, 'auth/change_profile.html', context)
