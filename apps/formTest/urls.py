from django.urls import path
import apps.formTest.views as views

urlpatterns = [
    path('form1', views.formTest),
    path('form0', views.form0),
    path('form2', views.form2),
    path('form3', views.form3),
    path('form4', views.form4),
    path('form5', views.form5),
    path('form6', views.form6),
    path('form7', views.form7),
    path('index2/', views.index,name="post_index"),
]
