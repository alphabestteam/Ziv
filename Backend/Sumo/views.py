from rest_framework import status
from .models import Sumo
from .serializers import SumoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAdminUser
from Gambler.decorators import get_gambler_from_token

 
class SumoView(APIView):

    @get_gambler_from_token
    @permission_classes([IsAdminUser]) 
    def post(self, request):
        serialized_sumo = SumoSerializer(data=request.data)
        if serialized_sumo.is_valid():
            serialized_sumo.save()
            return Response(serialized_sumo.data, status=status.HTTP_201_CREATED)
        return Response(serialized_sumo.errors, status=status.HTTP_400_BAD_REQUEST)

    @get_gambler_from_token
    def get(self, request):
        sumos = Sumo.objects.all()
        serialized_sumos = SumoSerializer(sumos, many=True)
        return Response(serialized_sumos.data, status=status.HTTP_200_OK)

    @get_gambler_from_token
    @permission_classes([IsAdminUser]) 
    def put(self, request):
        sumo_record = get_object_or_404(Sumo, id = request.data.get("id"))
        serialized_sumo = SumoSerializer(sumo_record, data=request.data, partial=True)
        if serialized_sumo.is_valid():
            serialized_sumo.save()
            return Response(serialized_sumo.data, status=status.HTTP_200_OK)
        return Response(serialized_sumo.errors, status=status.HTTP_400_BAD_REQUEST)

    @get_gambler_from_token
    @permission_classes([IsAdminUser]) 
    def delete(self, request):
        id = request.data.get("id")
        sumo = get_object_or_404(Sumo, pk=id)
        sumo.delete()
        return Response(f"Sumo has unregistered", status=200)

    
def update_rank_class(sumo, points):
    """
    The function receives a sumo ID and a point sum (either negative or positive)
    """
    sumo.points += points
    sumo.save()


