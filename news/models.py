from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('man', 'Мужской'),
        ('woman', 'Женский'),
        ('woman2', 'Улучшенный'),
        ('other', 'Другой'),
    )

    RACE_CHOICES = (
        ('human', 'Человек'),     
        ('elf', 'Эльф'),        
        ('demon', 'Демон'),       
        ('angel', 'Ангел'),       
        ('undead', 'Нежить'),     
        ('half_beast', 'Полузверь'),  
        ('other', 'Другое'),      
    )

    CLIENT = 'client'
    SALESMAN = 'salesman'
    ADMIN = 'admin'

    ROLE = (
        (CLIENT, 'Покупатель'),
        (SALESMAN, 'Продавец'),
        (ADMIN, 'Администратор')
    )
    role = models.CharField('роль', choices=ROLE, default=CLIENT, max_length=15)

    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True,verbose_name='Номер телефона')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True,verbose_name='Пол')
    race = models.CharField(max_length=10, choices=RACE_CHOICES, null=True, blank=True,verbose_name='Расса')

    groups = models.ManyToManyField('auth.Group', related_name='custom_user', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user', blank=True)

    def __str__(self):
        return self.username

class Avatar(models.Model):
    class Meta:
        verbose_name = "Аватар"
        verbose_name_plural = "Аватары"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="image",
        verbose_name="Фото ",
    )
    image = models.ImageField(upload_to="images/", verbose_name="Фото")

    def __str__(self):
        return f"{self.user.id}) Image of {self.user.username}"
class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return f'{self.id}) {self.name}'



class Post(models.Model):     
    class Meta:
        verbose_name='Посты' 
        ordering=['-id']
    title = models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Категория",
    )    
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tag", related_name="tags", verbose_name="Теги")
    views = models.IntegerField(default=0)
    location = models.URLField(verbose_name='Ссылка кафе', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id}) {self.title}'
    
    

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.score for rating in ratings) / ratings.count(), 2)
        return 0
    
    
class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self) -> str:
        return self.name
    
class UserProfile(models.Model):
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile",
        verbose_name="Профиль",
        default=User,
    )
    sold = models.PositiveIntegerField(verbose_name="Количество постов")
    followers = models.PositiveIntegerField(verbose_name="Количество подписчиков")
    bio = models.TextField(blank=True, null=True, verbose_name="Биография")

    def __str__(self):
        return self.user.username
    
class Rating(models.Model):
    class Meta:
        verbose_name='Рейтинг'
    post = models.ForeignKey(to=Post, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return f'{self.user} - {self.post} - {self.score}'

# class Comment(models.Model):
#     class Meta:
#         verbose_name='Коментарии' 
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     text = models.TextField(verbose_name='Текст коммента')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user} - {self.text[:30]}'
    

# Create your models here.
