from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import *
from news.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import *
from django import template

register = template.Library()

def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

# def workspace(request):
#     post=Post.objects.all()
#     #     paginator = Paginator(post, 5)  

#     context={
#         'page_obj':post
#     }
#     return render(request,'workspace/index.html',context)

@login_required
@register.filter(name='add_class')
def workspace(request):
    if not request.user.is_authenticated:
        messages.error(request, "Вы не авторизованы")
        return redirect('/')
    post = Post.objects.filter(author=request.user)
    paginator = Paginator(post, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    filterset = NewsFilter(data=request.GET, queryset=post)
    page_obj = filterset.qs
    context = {
        'page_obj': page_obj,
        'filterset':filterset
    }

    return render(request, 'workspace/index.html', context)


# from django.contrib import messages
# from .forms import PostForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user 
            post.save() 
            messages.success(request, 'Успешно')
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'workspace/create.html', {'form': form})

def update(request, id):
    post = get_object_or_404(Post, id=id)  
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успешно обновлен.')
            return redirect('/workspace/') 
    else:
        form = PostForm(instance=post)  
    return render(request, 'workspace/update.html', {'form': form})
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from .models import *
# from .forms import AnimeForm

# def edit_anime(request, pk):
#     anime = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = AnimeForm(request.POST, request.FILES, instance=anime)
#         if form.is_valid():
#             anime = form.save()
            
#             for image in request.FILES.getlist('images'):
#                 AnimeImage.objects.create(anime=anime, image=image)
            
#             messages.success(request, 'Аниме успешно обновлено.')
#             return redirect('anime_detail', pk=anime.pk)
#         else:
#             messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
#     else:
#         form = AnimeForm(instance=anime)

#     return render(request, 'edit_anime.html', {'form': form, 'anime': anime})



def delete(request, id):
    nft = get_object_or_404(Post, id=id) 
    nft.delete()

    return redirect('workspace') 
