from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description','is_active')
    list_filter = ('title',)
    ordering = ['title','description','is_active']
    search_fields = ('title','description','is_active')
