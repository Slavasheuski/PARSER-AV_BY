from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('refresh', views.refresh, name='refresh'),
    path('cars', views.cars, name="cars"),
    path('contacts', views.contacts, name="contacts"),
    path('news_home', views.news, name="news_home"),
]