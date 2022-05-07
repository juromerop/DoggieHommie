
from django.contrib import admin
from django.urls import path
from doggieHommie.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users',  UserCreateListView.as_view()),
    path('user/<int:pk>', UserRUDView.as_view()),
    path('login', LoginView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('bankAccount/create', BankAccountCreateListView.as_view()),
    path('bankAccount/<int:user>', BankAccountCreateListView.as_view()),
    path('post/', PostCreateView.as_view()),
    path('post/RUD/<int:pk>', PostRUDView.as_view()), 
    path('post/getAll', PostCreateListView.as_view()), 
    path('post/getByUser/<int:user>', PostByUserView().as_view()), 
]
