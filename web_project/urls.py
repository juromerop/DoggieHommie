
from django.contrib import admin
from django.urls import path
from doggieHommie.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users',  UserCreateListView.as_view()),
    path('user/<int:pk>', UserRUDView.as_view())

]
