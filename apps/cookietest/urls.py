from django.urls import path
import apps.cookietest.views as views

urlpatterns = [
    path('', views.index),
    path('setcookie/', views.set_cookie),
    path('getcookie/', views.get_cookie),
]
