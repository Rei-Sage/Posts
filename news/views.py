from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404


def get_artist_image(user):
    try:
        img = Avatar.objects.get(user=user)
        return img if img.image else None
    except Avatar.DoesNotExist:
        return None

def lending(request):
    post = Post.objects.all().order_by('-views')
    paginator = Paginator(post,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    context={
        'post':post,
        'page_obj':page_obj,   

    }
    return render(request,'index.html',context)


# def main(request):
#     news = News.objects.all()

#     search = request.GET.get('search')
#     if search:
#         news = news.filter(name__icontains=search)

#     category = request.GET.get('category')
#     if category:
#         category = Category.objects.get(id=int(category))
#         news = news.filter(category=category)

#     categories = Category.objects.all()
#     return render(request, 'index.html', {'news': news, 'categories': categories})


# def detail_news(request, id):
#     news = News.objects.get(id=id)
#     news.views += 1
#     news.save()
#     categories = Category.objects.all()
#     return render(request, 'detail_news.html', {'news': news, 'categories': categories})


# Create your views here.


def detail(request, id):
    posts = get_object_or_404(Post, id=id)
    post=Post.objects.filter(author=posts.author)


    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Нужно авторизоваться')
            return redirect('login')
        if 'rating' in request.POST:
            score = request.POST.get('rating')
            if score and score.isdigit():
                rating, created = Rating.objects.update_or_create(
                    post=posts,
                    user=request.user,
                    defaults={'score': int(score)}
                )
                # messages.success(request, 'Код 016 успешно')
            return redirect(f'/', id=id)

    paginator = Paginator(post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    post=Post.objects.filter(author=posts.author)
    posts.views += 1
    posts.save()



    return render(request, 'detail.html', {'page_obj': page_obj, 'categories': categories,'posts':posts})


@login_required
def profil(request):
    post=Post.objects.filter(author=request.user)
    img = get_artist_image(request.user)
    paginator = Paginator(post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        
        try:
            ava_image = Avatar.objects.get(user=request.user)
            ava_image.image = image
            ava_image.save()
        except ObjectDoesNotExist:
            Avatar.objects.create(user=request.user, image=image)
        
        return redirect('profil') 


    context = {
        'img': img,
        'post':post,
        'page_obj':page_obj
    }

    return render(request, 'user/profile.html', context)
from django.http import Http404



from django.http import Http404

def profil_users(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    post = Post.objects.filter(author=user)
    img = get_artist_image(user)
    paginator = Paginator(post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'img': img,
        'post': post,
        'page_obj': page_obj,
        'user':user
    }

    return render(request, 'user/user_profile.html', context)



def more(request):
    post=Post.objects.all()
    paginator = Paginator(post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    search = request.GET.get('search')
    if search is not None:
        page_obj = post.filter(title__icontains=search)
    context={
        'post':post,
        'page_obj':page_obj,
    }
    return render(request, 'post_more.html',context)


# @login_required
# def update_profile_picture(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         image = request.FILES['image']
        
#         try:
#             artist_image = ArtistImage.objects.get(artist=request.user)
#             artist_image.image = image
#             artist_image.save()
#         except ObjectDoesNotExist:
#             ArtistImage.objects.create(artist=request.user, image=image)
        
#         return redirect('profil')  

#     return render(request, 'profil.html')
