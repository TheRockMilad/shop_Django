from django.urls import path
import apps.blog.views as views

urlpatterns = [
    path("",views.index),
    path("authors",views.showAuthors),
    path("author/<int:author_id>",views.showAuthorsDetails)
]
