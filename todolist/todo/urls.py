from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/add/
    path('/add/', views.add, name='add'),
    # ex: /todo/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # save
    path('<int:pk>/save', views.save, name='save'),
    # delete
    path('<int:pk>/delete', views.delete, name='delete'),
]