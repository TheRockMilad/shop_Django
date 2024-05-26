from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    search_fields = ('name','email','message')