from django.urls import path
from django.conf.urls import url

from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<slug:title>/', views.wikiStats, name='wikiStats'),
    path('', views.wikiStats, name='wikiStats'),
]