# kush/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_person_form, name='create_person_form'),  # Changed URL pattern
    path('api/<int:user_id>/', views.get_person, name='get_person'),
    path('api/<int:user_id>/update/', views.update_person, name='update_person'),
    path('api/<int:user_id>/delete/', views.delete_person, name='delete_person'),
]
