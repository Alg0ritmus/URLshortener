from django.urls import path

from . import views

app_name = 'shortURL'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/post/',views.post_url,name='post_url'),
    path('api/get/<str:shorturl>/',views.get_url,name='get_url'),
]