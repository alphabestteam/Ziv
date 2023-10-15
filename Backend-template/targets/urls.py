from django.urls import path
from . import views

urlpatterns = [
    path('AddTarget/', views.add_target, name='add_target'),
    path('AllTargets/', views.all_targets, name='all_targets'),
    path('UpdateTarget/', views.update_target, name='update_target'),
]