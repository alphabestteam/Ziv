from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from people.models import Person
from people.serializers import PersonSerializer
from rest_framework import status


@csrf_exempt
def add_person(request):
    """
    The function receives a POST HTTP method
    The function extracts the JSON data
    The function serializes the data and creates a person
    A JSON response is sent out
    """
    if request.method == "POST":
        person_info = JSONParser().parse(request)
        name = person_info["name"]
        id = person_info["id"]
        birth_date = person_info["birth_date"]
        city = person_info["city"]
        person = Person.objects.create(
            id=id, name=name, city=city, birth_date=birth_date
        )
        person.save()
        person_data = PersonSerializer(person).data
        return JsonResponse(person_data, status=status.HTTP_200_OK)
    else:
        return JsonResponse(
            {"Your HTTP request is not of type POST, your method is not allowed"},
            status=405,
        )


@csrf_exempt
def update_person(request, id):
    """
    The function receives an UPDATE HTTP request
    The function extracts the JSON data
    The function serializes the data and updates the matching person
    A JSON response is sent out
    """
    if request.method == "PUT":
        person_info = JSONParser().parse(request)
        person = Person.objects.get(id=id)
        data_deserialized = PersonSerializer(person, data=person_info)
        if data_deserialized.is_valid():
            person.name = person_info["name"]
            person.birth_date = person_info["birth_date"]
            person.city = person_info["city"]
            person.save()
            return JsonResponse(data_deserialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(
                data_deserialized.errors, status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return JsonResponse(
            {"Your HTTP request is not of type PUT, your method is not allowed"},
            status=405,
        )


def all_people(request):
    """
    The function receives a GET HTTP request
    The function returns a JSON response of all existing Person records
    """
    if request.method == "GET":
        targets = Person.objects.all()
        serializer = PersonSerializer(targets, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        )


def remove_person(request, id):
    """
    The function receives a DELETE HTTP request
    The function deletes the specified record from the database
    If the record doesn't exist, a 404 error is thrown
    """
    if request.method == "DELETE":
        person = get_object_or_404(Person, pk=id)
        person.delete()
        return HttpResponse(f"Person number {id} has been deleted", status=200)
    else:
        return JsonResponse(
            {"Your HTTP request is not of type DELETE, your method is not allowed"},
            status=405,
        )
