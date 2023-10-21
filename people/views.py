from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from people.models import Person, Parent
from people.serializers import PersonSerializer, ParentSerializer, ParentNamesSerializer
from rest_framework import status
from datetime import date, timedelta


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
        serialized_person = PersonSerializer(data = person_info)
        id = person_info["id"]
        if serialized_person.is_valid():
            if id is not None:
                serialized_person.validated_data['id'] = id
            serialized_person.save()
            return JsonResponse(serialized_person.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(
            {"Your HTTP request is not of type POST, your method is not allowed"},
            status=405,
        )


def update_person(request, id):
    """
    The function receives an UPDATE HTTP request
    The function extracts the JSON data
    The function serializes the data and updates the matching person
    A JSON response is sent out
    """
    if request.method == "PUT":
        person_info = JSONParser().parse(request)
        person = get_object_or_404(Person, pk = id)
        serialized_person = PersonSerializer(instance = person, data = person_info, partial=True)
        if serialized_person.is_valid():
            serialized_person.save()
            return JsonResponse(serialized_person.data, status = status.HTTP_200_OK, safe=False)
        return JsonResponse(serialized_person.errors, status=400)
    else:
        return HttpResponse(
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
        return HttpResponse(
            {"Your HTTP request is not of type DELETE, your method is not allowed"},
            status=405,
        )
    

@csrf_exempt
def add_parent(request):
    """
    The function receives a POST HTTP method
    The function extracts the JSON data
    The function serializes the data and creates a parent
    A JSON response is sent out
    """
    if request.method == "POST":
        parent_info = JSONParser().parse(request)
        serialized_parent = ParentSerializer(data=parent_info)
        id = parent_info.get("id")

        if serialized_parent.is_valid():
            if id is not None:
                serialized_parent.validated_data['id'] = id
            serialized_parent.save()
            return JsonResponse(serialized_parent.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized_parent.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(
            "Your HTTP request is not of type POST, your method is not allowed",
            status=405
        )
    

@csrf_exempt
def update_parent(request, id):
    """
    The function receives an UPDATE HTTP request
    The function extracts the JSON data
    The function serializes the data and updates the matching parent
    A JSON response is sent out
    """
    if request.method == "PUT":
        person_info = JSONParser().parse(request)
        parent = get_object_or_404(Parent, id = person_info["id"])
        serialized_parent = ParentSerializer(instance=parent, data = person_info, partial=True)
        if serialized_parent.is_valid():
            serialized_parent.save()
            return JsonResponse(serialized_parent.data, status=status.HTTP_200_OK, safe=False)
        return JsonResponse(serialized_parent.errors, status=400)
    else:
        return HttpResponse(
            {"Your HTTP request is not of type PUT, your method is not allowed"},
            status=405,
        )



def all_parents(request):
    """
    The function receives a GET HTTP request
    The function returns a JSON response of all existing Parent records
    """
    if request.method == "GET":
        parent = Parent.objects.all()
        serializer = ParentSerializer(parent, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        )
    
def remove_parent(request, id):
    """
    The function receives a DELETE HTTP request
    The function deletes the specified record from the database
    If the record doesn't exist, a 404 error is thrown
    """
    if request.method == "DELETE":
        parent = get_object_or_404(Parent, pk=id)
        parent.delete()
        return HttpResponse(f"Parent number {id} has been deleted", status=200)
    else:
        return HttpResponse(
            {"Your HTTP request is not of type DELETE, your method is not allowed"},
            status=405,
        )
    
def get_specified_parent(request, id):
    """
    The function receives a GET HTTP request and id
    The function returns a JSON response of the specified Parent and all of its children 
    """
    if request.method == "GET":
        parent = get_object_or_404(Parent, pk=id)
        serialized_parent = ParentSerializer(parent)
        children = parent.children.all()
        serialized_children = PersonSerializer(children, many=True).data
        parent_data = serialized_parent.data
        parent_data['children'] = serialized_children
        return JsonResponse(parent_data, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        )

def child_parent_connector(request):
    """
    The function receives a GET request
    The function extracts two ids from the JSON of the request
    The function adds one id to the children field of the other id
    """
    if request.method == "PUT":
        request_info = JSONParser().parse(request)
        parent = get_object_or_404(Parent, pk=request_info["parent_id"])
        child = get_object_or_404(Person, pk=request_info["child_id"])
        parent.children.add(child)
        parent.save()
        return HttpResponse({"The child now belongs to the parent"},status=201)
    else:
        return HttpResponse(
            {"Your HTTP request is not of type PUT, your method is not allowed"},
            status=405,
        )
    

def rich_children_query(request):
    """
    The function filters all the people who:
    - are under eighteen
    - have at least one parent who makes over 50000
    The function returns a JSON response of all those children
    """
    if request.method == "GET":
        eighteen_years_ago = date.today() - timedelta(days=365 * 18)
        children = Person.objects.filter(
            birth_date__gt = eighteen_years_ago,
            parents__salary__gte = 50000,         
            parents__isnull = False               
        ).distinct()
        serializer = PersonSerializer(children, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        )

def get_parents_names(request, id):
    """
    The function receives a GET request and an id
    The function gets all the parents of the specified person
    The function returns a least of the parents' names
    """
    if request.method == "GET":
        child = get_object_or_404(Person, id=id)
        parents = child.parents.all()
        parent_names = [parent.name for parent in parents]
        return JsonResponse({'Parents': parent_names})
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        )
    
def parents_names_with_serializers(request, id):
    """
    The function receives a GET request and an id
    The function gets all the parents of the specified person
    The function returns a least of the parents' names
    This variation of the function must use serializers
    """
    if request.method == "GET":
        child = Person.objects.get(id=id)
        parents_list = child.parents.all()
        serialized_parents =  ParentNamesSerializer(parents_list, many=True)
        parent_names = [parent['name'] for parent in serialized_parents.data]
        return JsonResponse({'Parents': parent_names}, status=status.HTTP_200_OK)
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        )
    


def get_children_names(request, id):
    """
    The function receives a GET request and an id
    The function gets all the parents of the specified person
    The function returns a least of the parents' names
    """
    if request.method == "GET":
        person = get_object_or_404(Person, id=id)
        children = person.children.all()
        children_data = []
        for child in children:
            serializer = PersonSerializer(child)
            children_data.append(serializer.data)
        return JsonResponse(children_data)
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        ) 

def get_grandparents_names(request, id):
    """
    The function receives a GET request and an id
    The function gets all the grandparents of the specified person
    The function returns a least of the grandparents' names
    """
    if request.method == "GET":
        person = get_object_or_404(Person, id=id)
        parents_list = person.parents.all()
        grandparents_names = []
# A nested loop is need to iterate over all the grandparents (parents of each of the person's parents)
        for parent in parents_list:
            grandparents_list = parent.parents.all()
            for grandparent in grandparents_list:
                grandparents_names.append(grandparent.name)

        return JsonResponse({'Grandparents': grandparents_names})
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        ) 
    
def get_siblings_names(request, id):
    """
    The function receives a GET request and an id
    The function gets all the siblings of the specified person
    The function returns a least of the siblings' names
    """
    if request.method == "GET":
        person = get_object_or_404(Person, id=id)
        siblings_names = []
        parents_list = person.parents.all()
        for parent in parents_list:
            siblings_list= parent.children.exclude(id=id)
            sibling_names = [sibling.name for sibling in siblings_list]
            siblings_names.extend(sibling_names)
        return JsonResponse({'Siblings': siblings_names})
    else:
        return HttpResponse(
            "Your HTTP request is not of type GET, your method is not allowed",
            status=405,
        ) 