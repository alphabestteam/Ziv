from django.urls import path
from . import views
from .views import add_collaborator


urlpatterns = [
    path('records/', views.RecordView.as_view(), name='create'),
    path('records/<int:user_id>/<int:record_id>/', views.RecordView.as_view(), name='delete-update-get'),
    path('records/add_collaborator/<int:file_id>/', add_collaborator, name='add-collaborator'),

    ]