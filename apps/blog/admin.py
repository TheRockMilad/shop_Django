from django.contrib import admin
from .models import Author,Article,Publication,chiefEditor

# Register your models here.

@admin.register(Author)
class Authoradmin(admin.ModelAdmin):
    list_display = ('name','family','age','register_date','is_active')
    list_filter = ('family','is_active')
    search_fields = ('family','name','age')
    ordering = ["family","name"]
    prepopulated_fields = {"url":('name','family')}

# admin.site.register(Author,Authoradmin)

#---------------------------------------

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title','create_at','is_active','status','author')

# ---------------------------------------

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title','chiefEditor')

#---------------------------------------

@admin.register(chiefEditor)
class ChiefEditorAdmin(admin.ModelAdmin):
    list_display = ('name','family','publication')
