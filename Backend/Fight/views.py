from rest_framework import status
from .serializers import FightSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
import random
from Sumo.views import update_rank_class
from Gamble.views import manage_all_fight_gambles
from Gambler.decorators import get_gambler_from_token
from Sumo.models import Sumo
from .models import Fight  


class StartFight(APIView):

    @get_gambler_from_token
    @permission_classes([IsAdminUser])
    def put(self, request):
        """
        Start a fight and resolve its winner, update ranks, manage gambles, and return a success message.
        """
        fight_id = request.data.get("id")
        fight_record = get_object_or_404(Fight, id=fight_id)

        challenging_sumo = Sumo.objects.get(pk=fight_record.challenging_sumo.id)
        opponent_sumo = Sumo.objects.get(pk=fight_record.opponent_sumo.id)

        challenger_score = challenging_sumo.points * random.randint(1, 10)
        opponent_score = opponent_sumo.points * random.randint(1, 10)

        if challenger_score > opponent_score:
            fight_record.winner = challenging_sumo
            update_rank_class(challenging_sumo, fight_record.fight_rank)
        elif challenger_score < opponent_score:
            fight_record.winner = opponent_sumo
            update_rank_class(opponent_sumo, fight_record.fight_rank)
        else:
            fight_record.winner = random.choice([challenging_sumo, opponent_sumo])

        fight_record.save()

        manage_all_fight_gambles(fight_id)

        return Response(f'Fight {fight_id} has been resolved. The winner was {fight_record.winner.id}', status=status.HTTP_200_OK)


class FightView(APIView):

    @get_gambler_from_token
    def get(self, request):
        # This function is  accessible to any authenticated user (gambler)
        fights = Fight.objects.all()
        serialized_fights = FightSerializer(fights, many=True)
        return Response(serialized_fights.data, status=status.HTTP_200_OK)

    @get_gambler_from_token
    @permission_classes([IsAdminUser]) 
    def post(self, request):
        serialized_fight = FightSerializer(data=request.data)
        if serialized_fight.is_valid():
            serialized_fight.save()
            return Response(serialized_fight.data, status=status.HTTP_201_CREATED)
        return Response(serialized_fight.errors, status=status.HTTP_400_BAD_REQUEST)

    @get_gambler_from_token
    @permission_classes([IsAdminUser])
    def put(self, request, *args, **kwargs):
        fight_record = get_object_or_404(Fight, id=request.data.get('id'))
        serialized_fight = FightSerializer(fight_record, data=request.data, partial=True)
        if serialized_fight.is_valid():
            serialized_fight.save()        
            return Response('Fight has been updated', status=status.HTTP_200_OK)
        else: 
            return Response(serialized_fight.errors, status=status.HTTP_400_BAD_REQUEST)


    @get_gambler_from_token
    @permission_classes([IsAdminUser])
    def delete(self, request):
        fight = get_object_or_404(Fight, pk=request.data.get("id"))
        fight.delete()
        manage_all_fight_gambles(request.data.get("id"))
        return Response(f"Fight has been canceled", status=200)
