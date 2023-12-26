from django.urls import path
from .views import GambleView, manage_all_fight_gambles
from . import views

urlpatterns = [
    path('gambles/', views.GambleView.as_view(), name='gambles'),
]
