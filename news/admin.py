from django.contrib import admin
from .models import *
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Avatar)

admin.site.register(Rating)


# # Регистрация модели Category
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')  # Какие поля показывать в списке
#     search_fields = ('name',)  # Возможность поиска по имени категории
#     list_filter = ('name',)  # Фильтрация по имени

# admin.site.register(Category, CategoryAdmin)

# # Регистрация модели Tag
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')  # Какие поля показывать в списке
#     search_fields = ('name',)  # Возможность поиска по имени тега

# admin.site.register(Tag, TagAdmin)

# # Регистрация модели Post
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'created_at', 'views', 'author')  # Поля для отображения
#     list_filter = ('category', 'created_at', 'author')  # Фильтрация по этим полям
#     search_fields = ('title', 'description')  # Поиск по этим полям
#     readonly_fields = ('created_at',)  # Сделать поле "created_at" доступным только для чтения

# admin.site.register(Post, PostAdmin)

# # Регистрация модели UserProfile
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'sold', 'followers', 'bio')  # Отображаемые поля
#     search_fields = ('user__username',)  # Поиск по имени пользователя
#     list_filter = ('sold', 'followers')  # Фильтрация по количеству постов и подписчиков

# admin.site.register(UserProfile, UserProfileAdmin)

# # Регистрация модели Comment
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'post', 'created_at', 'text')  # Отображаемые поля
#     search_fields = ('user__username', 'post__title')  # Поиск по имени пользователя и названию поста
#     list_filter = ('created_at', 'post')  # Фильтрация по дате и посту

# admin.site.register(Comment, CommentAdmin)

