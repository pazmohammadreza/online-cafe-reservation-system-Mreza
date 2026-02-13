from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('reservation_list/', views.reservation_lists, name='reservation_lists'),
    path('reservation_list/pending/', views.pending_list, name='pending_list'),
    path('reservation_list/confirmed/', views.confirmed_list, name='confirmed_list'),
    path('reservation_list/cancelled/', views.cancelled_list, name='cancelled_list'),
    path('reservation_list/completed/', views.completed_list, name='completed_list'),
]