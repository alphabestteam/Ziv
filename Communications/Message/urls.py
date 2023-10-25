from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageView.as_view(), name='create-get'),
    path('messages/<int:user_id>/<int:message_id>/', views.MessageView.as_view(), name='delete-update')
    ]