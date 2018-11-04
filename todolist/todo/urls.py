from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/add/
    path('/add/', views.add, name='add'),
    # ex: /todo/1/edit/
    path('<int:todolist_id>/edit/', views.edit, name='edit'),
    # save
    path('<int:todolist_id>/save/', views.save, name='save'),
    # delete
    path('<int:todolist_id>/delete/', views.delete, name='delete'),
]