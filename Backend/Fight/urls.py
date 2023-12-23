from django.urls import path
from . import views

urlpatterns = [
    path('fights/start_fight/', views.StartFight.as_view(), name='start_fight'),
    path('fights/', views.FightView.as_view(), name='fight_list'),
]
