from django.contrib import admin
from django.urls import path, include
from mywed import views


urlpatterns = [

    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login', views.login , name='login'),
]
