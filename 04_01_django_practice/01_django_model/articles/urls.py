from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # articles/
    path('', views.index, name='index'),

    # articles/new/ -> throw
    path('new/', views.new, name='new'),

    path('create/', views.create, name='create'),
]