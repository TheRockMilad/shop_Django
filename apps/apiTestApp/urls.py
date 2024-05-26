from django.urls import path
import apps.apiTestApp.views as views
from rest_framework.authtoken import views as auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('',views.index,name='index')
    path('index', views.api_index, name='api_index'),
    path('indexapi', views.IndexApi.as_view()),
    path('indexapi2/<str:name>/<str:family>/<int:age>', views.IndexApi2.as_view()),
    path('indexapi3/', views.IndexApi3.as_view()),
    path('people/', views.PersonList.as_view()),
    path('people/<int:code>', views.SearchPersonById.as_view()),
    path('people/add/', views.PersonAdd.as_view()),
    path('product/add/', views.ProductAdd.as_view()),
    # برای دریافت توکن
    path('api-token-auth/', auth_token.obtain_auth_token),
    path('create-token/', views.CreateTokenForAllUser.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/delete/<int:pk>', views.DeleteProductFeature.as_view()),
    # برای دریافت token از طریق jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
