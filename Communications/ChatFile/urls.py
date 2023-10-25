from django.urls import path
from .views import ChatFileView, add_collaborator, add_message

urlpatterns = [
    path('chatFile/', ChatFileView.as_view(), name='create'),
    path('chatFile/<int:user_id>/<int:file_id>/', ChatFileView.as_view(), name='delete-update-get'),
    path('chatFile/add_collaborator/<int:file_id>/', add_collaborator, name='add-collaborator'),
    path('chatFile/add_message/<int:file_id>/', add_message, name='add-message'),

]

