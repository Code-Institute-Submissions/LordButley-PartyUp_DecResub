from django.contrib import admin
from .models import Post, Comment, Games
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('created_on',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created_on',)

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_filter = ('id',)

    



# admin.site.register(Post)