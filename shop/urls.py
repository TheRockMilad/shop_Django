"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path("admin/", admin.site.urls),
      path('', include('apps.mainapp.urls')),
      path('blog/', include('apps.blog.urls')),
      path('forms/', include('apps.formTest.urls')),
      path('viewtest/',include('apps.viewtest.urls')),
      path('blog2/',include('apps.blog2.urls')),
      path('cookietest/',include('apps.cookietest.urls'),name="redirect"),
      path('sessiontest/',include('apps.sessiontest.urls')),
      path('ajaxtest/',include('apps.ajaxtest.urls')),
      path('api/',include('apps.apiTestApp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "پنل مدیریت فروشگاه"
admin.site.index_title = "به پنل مدیریت خوش آمدید"
