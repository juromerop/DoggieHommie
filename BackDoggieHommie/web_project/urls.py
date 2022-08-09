
from django.contrib import admin
from django.urls import path
from doggieHommie.views.UserDetail import UserDetailAPIView
from doggieHommie.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users',  UserCreateListView.as_view()),
    path('user/<int:pk>', UserRUDView.as_view()),
    path('login', LoginView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('bankAccount/create', BankAccountCreateListView.as_view()),
    path('bankAccount/<int:pk>', BankAccountCreateListView.as_view()),
    # path('updateUser', UpdateUserView),
    path('updateUser/<int:pk>', UserRUDView.as_view()),
    path('bankAccount/<int:user>', BankAccountCreateListView.as_view()),
    path('post/', PostCreateView.as_view()),
    path('post/RUD/<int:pk>', PostRUDView.as_view()), 
    path('post/getAll', PostCreateListView.as_view()), 
    path('post/getByUser/<int:user>', PostByUserView.as_view()),
    path('comment/create', CommentCreateList.as_view()),
    path('user/report/<int:pk>', UserRUDView.as_view()),
    path('post/deshabilitar/<int:pk>', PostUpdateView.as_view()),
    path('notification/getAll/<int:user>',  NotificationListView.as_view()),
    # path('upvotePost', UserRUDView.as_view()),
]
