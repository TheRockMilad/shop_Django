from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="blog_index"),
    path('add', Create_blog, name="Create_blog")
]
