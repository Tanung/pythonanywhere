from django.contrib import admin
from django.urls import path,include
from mywed import views

urlpatterns = [
    path('', views.index),
    #path('polls/', include('polls.urls')),
    path('mywed/', include('mywed.urls')),
    path('united', views.united),
    path('admin/', admin.site.urls),
]
