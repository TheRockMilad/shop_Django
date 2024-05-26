from django.urls import path
from apps.viewtest.views import *

urlpatterns = [
    path('form0', fun0),
    path("form1", ViewClass1.as_view(), ),
    path('add', PostCreate.as_view(), name="PostCreate"),
    path('list', PostList.as_view(), name="ShowList"),
    path('detail/<int:pk>', PostDetail.as_view(), name="PostDetail"),
    path('update/<int:pk>', PostUpdate.as_view(), name="PostUpdate"),
    path('delete/<int:pk>', PostDelete.as_view(), name="PostDelete"),
    path('page2', GenericClass1.as_view(), name="ShowList2"),
    path('page3', GenericClass3.as_view(), name="ShowList3"),
    path('page4', fun1, name="showlist4"),
    path('page5/', GenericClass5.as_view(), name="ShowList5"),
]
