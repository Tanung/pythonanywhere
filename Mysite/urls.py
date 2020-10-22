from django.contrib import admin
from django.urls import path
from mywed import views


urlpatterns = [

    path('', views.index, name='index'),
    path('index_user', views.index_user, name='index_user'),
    path('admin/', admin.site.urls),
    path('animal', views.animal, name='animal'),
    path('animal_user', views.animal_user, name='animal_user'),
    path('add_animal', views.add_animal, name='add_animal'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),

    #path('Upload', views.Upload),
]
