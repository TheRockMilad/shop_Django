from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog2
        fields = ['title','descrioption','is_active','main_img']
        
        

