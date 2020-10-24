from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('index_user', views.index_user, name='index_user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('animal', views.animal, name='animal'),
    path('animal_user', views.animal_user, name='animal_user'),
    path('add_animal', views.add_animal, name='add_animal'),
    path('allanimal',views.allanimal, name='allanimal'),

    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]