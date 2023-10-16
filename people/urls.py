from django.urls import path, re_path
from . import views

urlpatterns = [
    path("addPerson/", views.add_person, name="add_person"),
    path("getAllPeople/", views.all_people, name="all_people"),
    path("removePerson/<int:id>", views.remove_person, name="remove_person"),
    path("updatePerson/<int:id>/", views.update_person, name="update_person"),
]
