from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts admin model"""
    list_display = ('pk', 'user', 'title', 'photo')
    list_filter = ('date_created', 'date_modified')