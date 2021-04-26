from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_main, name='main'),
    path('memories/', views.render_memories, name='memories'),
    path('add_memory/', views.add_memory, name='add_memory'),
    path('change_memory/<int:pk>/', views.change_memory, name='change_memory'),
    path('delete_memory/<int:pk>/', views.delete_memory, name='delete_memory')
]
