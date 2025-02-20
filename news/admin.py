from django.contrib import admin
from .models import *
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(UserProfile)
# admin.site.register(Comment)
admin.site.register(Avatar)

admin.site.register(Rating)



# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name') 
#     search_fields = ('name',)  
#     list_filter = ('name',)  

# admin.site.register(Category, CategoryAdmin)

# class TagAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')  
#     search_fields = ('name',)  

# admin.site.register(Tag, TagAdmin)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'created_at', 'views', 'author')  
#     list_filter = ('category', 'created_at', 'author')  
#     search_fields = ('title', 'description')  
#     readonly_fields = ('created_at',)  

# admin.site.register(Post, PostAdmin)

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'sold', 'followers', 'bio')  
#     search_fields = ('user__username',)  
#     list_filter = ('sold', 'followers')  

# admin.site.register(UserProfile, UserProfileAdmin)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'post', 'created_at', 'text')  
#     search_fields = ('user__username', 'post__title')  
#     list_filter = ('created_at', 'post')  

# admin.site.register(Comment, CommentAdmin)

