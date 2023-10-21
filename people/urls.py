from django.urls import path
from . import views

urlpatterns = [
    path("addPerson/", views.add_person, name="add_person"),
    path("getAllPeople/", views.all_people, name="all_people"),
    path("removePerson/<int:id>/", views.remove_person, name="remove_person"),
    path("updatePerson/<int:id>/", views.update_person, name="update_person"),

    path("addParent/", views.add_parent, name="add_parent"),
    path("getAllParents/", views.all_parents, name="all_parents"),
    path("removeParent/<int:id>/", views.remove_parent, name="remove_parent"),
    path("updateParent/<int:id>/", views.update_parent, name="update_parent"),

    path("getSpecifiedParent/<int:id>/", views.get_specified_parent, name="get_specified_parent"),
    path("childParentConnector/", views.child_parent_connector, name="child_parent_connector"),
    path("richChildrenQuery/", views.rich_children_query, name="rich_children_query"),
    path("getParentsNames/<int:id>/", views.get_parents_names, name="get_parents_names"),
    path("parentsNamesWithSerializers/<int:id>/", views.parents_names_with_serializers, name="parents_names_with_serializers"),
    path("getChildrenNames/<int:id>/", views.get_children_names, name="get_children_names"),
    path("getGrandparentsNames/<int:id>/", views.get_grandparents_names, name="get_grandparents_names"),
    path("getSiblingsNames/<int:id>/", views.get_siblings_names, name="get_siblings_names"),
]


