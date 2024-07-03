from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:id>/', views.note_detail, name='note_detail'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/<int:id>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:id>/delete/', views.note_delete, name='note_delete'),
    path('note/<int:id>/pin/', views.note_pin, name='note_pin'),
    path('note/<int:id>/move_up/', views.note_move_up, name='note_move_up'),
    path('note/<int:id>/move_down/', views.note_move_down, name='note_move_down'),
    path('note/admin/', admin.site.urls)
]
