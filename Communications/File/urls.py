from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.FileView.as_view(), name='create'),
    path('files/<int:user_id>/<int:file_id>/', views.FileView.as_view(), name='delete-update-get'),
    path('files/add_collaborator/<int:file_id>/', views.add_collaborator, name='add_collaborator'),
    ]