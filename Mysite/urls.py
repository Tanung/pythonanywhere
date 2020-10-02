from django.contrib import admin
from django.urls import path, include
from mywed import views


urlpatterns = [

    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
]
