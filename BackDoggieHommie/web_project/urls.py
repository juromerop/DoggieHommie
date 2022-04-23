
from django.contrib import admin
from django.urls import path
from doggieHommie.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users',  UserCreateListView.as_view()),
    path('user/<int:pk>', UserRUDView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    
]
