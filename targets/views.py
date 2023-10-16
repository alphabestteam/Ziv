import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from targets.models import Target
from targets.serializers import TargetSerializer
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
def add_target(request):
    """
    The function receives a POST HTTP method
    """
    if request.method == "POST":
        target_info = JSONParser().parse(request)
        target = Target(
            name=target_info["name"],
            attack_priority=target_info["attack_priority"],
            latitude=target_info["latitude"],
            longitude=target_info["longitude"],
            enemy_organization=target_info["enemy_organization"],
            target_goal=target_info["target_goal"],
            was_target_destroyed=target_info.get("was_target_destroyed", False),
            target_id=target_info.get("target_id", None),
            )
        data_deserialized = TargetSerializer(data = target_info)
        if data_deserialized.is_valid():
            target.save()
            return JsonResponse(data_deserialized.data, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(data_deserialized.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
       return JsonResponse(
            {"Your HTTP request is not of type POST, your method is not allowed"},
            status=405,
        )

@csrf_exempt
def update_target(request):
    if request.method == "PUT":
        target_info = JSONParser().parse(request)
        print(target_info)
        target = Target.objects.get(target_id = target_info.get('target_id', None))
        print(target)
        data_deserialized = TargetSerializer(target, data = target_info)
        if data_deserialized.is_valid():
            target.name = target_info["name"]
            target.attack_priority = target_info["attack_priority"]
            target.latitude = target_info["latitude"]
            target.longitude = target_info["longitude"]
            target.enemy_organization = target_info["enemy_organization"]
            target.target_goal = target_info["target_goal"]
            target.was_target_destroyed = target_info["was_target_destroyed"]
            target.save()
            return JsonResponse(data_deserialized.data, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse(data_deserialized.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse(
            {"Your HTTP request is not of type PUT, your method is not allowed"},
            status=405,
        )


def all_targets(request):
    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe = False)
    else:
        return JsonResponse(
            {"Your HTTP request is not of type GET, your method is not allowed"},
            status=405,)
    
