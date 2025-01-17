from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('event/<int:id>', views.update_event, name='update_event'),

]