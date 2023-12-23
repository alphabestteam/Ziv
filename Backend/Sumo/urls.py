from django.urls import path
from . import views

urlpatterns = [
    path('sumo/', views.SumoView.as_view(), name='sumo_list'),
]