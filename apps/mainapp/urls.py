from django.urls import path
import apps.mainapp.views as views

urlpatterns = [
    path('',views.index),
    path('step2/',views.step2),
    path('step3/',views.step3),
    path('step4/',views.step4),
    path('step5/',views.step5),
    path('step6/',views.step6),
    path('step7/',views.step7),
    path('step8/',views.step8,name="template8"),
    path('step9/',views.step9,name="template9"),
    path('step10/',views.step10,name="template10"),
    path('step11/',views.step11,name="template11"),
]
