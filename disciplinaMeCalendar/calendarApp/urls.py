from django.urls import path
from . import views

urlpatterns = [
    path('activities/', views.ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', views.ActivityRetrieveUpdateDestroyView.as_view(), name='activity-retrieve-update-destroy'),
    ]
