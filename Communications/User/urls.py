from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='create-get'),
    path('users/<int:id>/', views.UserView.as_view(), name='delete-update'),
    path('users/clear_inbox/<int:id>/', views.clear_inbox, name='clear_inbox'),
    ]