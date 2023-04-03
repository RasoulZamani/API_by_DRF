from django.urls import path
from rest_framework.authtoken import views as token_views
from . import views
from rest_framework import routers


app_name='accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('api-token-auth/', token_views.obtain_auth_token),
]

# router for UserViewSet .../user/...
router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls