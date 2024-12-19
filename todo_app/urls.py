from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),  # Home page for listing to-do lists
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='list'),  # List view for each to-do list
    path('list/add/', views.ListCreate.as_view(), name='list-add'),  # Add a new to-do list
    path('list/<int:list_id>/item/add/', views.ItemCreate.as_view(), name='item-add'),  # Add a new to-do item
    path('list/<int:list_id>/item/<int:pk>/edit/', views.ItemUpdate.as_view(), name='item-edit'),  # Edit an item
    path('list/<int:list_id>/delete/', views.ListDelete.as_view(), name='list-delete'),  # Delete a list
    path('list/<int:list_id>/item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),  # Delete an item
]
