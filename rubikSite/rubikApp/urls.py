from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path('twoByTwo/', views.twoByTwo, name='twoByTwo'),
    re_path('clearCache/', views.clearCache, name='clearCache'),
]