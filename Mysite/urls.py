from django.contrib import admin
from django.urls import path,include
from mywed import views

urlpatterns = [
    path('', views.Homepage),
    path('History/', views.History ,name='History'),
    path('h1/', views.h1 ,name='h1'),
    path('h2/', views.h2 ,name='h2'),
    path('h3/', views.h3 ,name='h3'),
    path('h4/', views.h4 ,name='h4'),
    path('h5/', views.h5 ,name='h5'),

    path('Culture/', views.Culture ,name='Culture'),
    path('c1/', views.c1 ,name='c1'),
    path('c2/', views.c2 ,name='c2'),
    path('c3/', views.c3 ,name='c3'),
    path('c4/', views.c4 ,name='c4'),


    path('Planet/', views.Planet ,name='Planet'),
    path('Science/', views.Science ,name='Science'),
    path('Communities/', views.Communities ,name='Communities'),
    #path('mywed/History/', views.History, name='History'),
    #path('polls/', include('polls.urls')),
    #path('mywed/', include('mywed.urls')),
    #path('united', views.united),
    path('admin/', admin.site.urls),
]
