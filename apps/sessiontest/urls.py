from django.urls import path
from apps.sessiontest import views

urlpatterns = [
    path('', views.index),
    path('setsession', views.set_session),
    path('getsession', views.get_session),
    path('deletesession', views.delete_session),
]
