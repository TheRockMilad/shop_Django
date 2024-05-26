from django.urls import path
import apps.ajaxtest.views as views

urlpatterns = [
    path('index',views.index),
    path('like/',views.like,name='like'),
    path('contact/',views.contact_form,name='contact'),
]

