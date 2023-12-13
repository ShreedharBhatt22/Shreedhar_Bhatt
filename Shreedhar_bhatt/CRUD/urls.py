# contacts/urls.py
from django.urls import path
from . import views
from .views import new_contact,edit_contact,delete_contact

urlpatterns = [
    path('', views.home, name='home'),
    path('create',new_contact, name='new_contact'),
    path('CRUD/<int:contact_id>/', views.contact_details, name='contact_details'),
    path('CRUD/<int:contact_id>/update/', edit_contact, name='update_contact'),
    path('CRUD/<int:contact_id>/delete/', delete_contact, name='delete_contact'),
]