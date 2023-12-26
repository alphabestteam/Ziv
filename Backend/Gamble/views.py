from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Gamble
from .serializers import GambleSerializer
from django.db import transaction
from Fight.models import Fight
from Gambler.decorators import get_gambler_from_token


class GambleView(APIView):

    @get_gambler_from_token
    def get(self, request):
        gambler = self.gambler 
        gambles = gambler.gambles.all() 
        serialized_gambles = GambleSerializer(gambles, many=True)
        return Response(serialized_gambles.data, status=status.HTTP_200_OK)

    def update_gambler_account(self, gambler, amount):
        with transaction.atomic():
            gambler.account_balance += amount
            gambler.save()

    def add_gamble(self, gambler, gamble):
        """
        Add a gamble to the gambler's gambles property.
        """
        assumed_winner_id = gamble.data['assumed_winner']
        
        new_gamble = Gamble.objects.create(
            fight_id=gamble.instance.fight_id,
            assumed_winner_id=assumed_winner_id,
            bet_amount=gamble.data['bet_amount']
        )

        # Add the new gamble to the gambler's gambles
        gambler.gambles.add(new_gamble)
        gambler.save()


            
    
    @get_gambler_from_token
    def post(self, request):
        gambler = self.gambler  
        serialized_gamble = GambleSerializer(data=request.data)
        if serialized_gamble.is_valid():
            bet_amount = request.data.get('bet_amount', 0.0)
            if gambler.account_balance >= bet_amount:
                self.update_gambler_account(gambler, -(bet_amount))  # Reduce balance
                serialized_gamble.save()
                self.add_gamble(gambler, serialized_gamble)  # Add the gamble to gambler's gambles
                return Response(serialized_gamble.data, status=status.HTTP_201_CREATED)
            else:
                return Response('Insufficient funds', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serialized_gamble.errors, status=status.HTTP_400_BAD_REQUEST)



    @get_gambler_from_token
    def put(self, request):
        gambler = self.gambler
        gamble = get_object_or_404(Gamble, id=request.data.get('id'))
        old_bet_amount = gamble.bet_amount
        serialized_gamble = GambleSerializer(gamble, data=request.data, partial=True)

        if serialized_gamble.is_valid():
            new_bet_amount = request.data.get('bet_amount', 0.0)
            diff_amount = new_bet_amount - old_bet_amount

            if gambler.account_balance >= diff_amount:
                self.update_gambler_account(gambler, -diff_amount)
                serialized_gamble.save()
                return Response({'detail': 'Gamble has been updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
        print(serialized_gamble.errors)
        return Response({'error': serialized_gamble.errors}, status=status.HTTP_400_BAD_REQUEST)


    @get_gambler_from_token
    def delete(self, request):
        gambler = self.gambler
        gamble_id = request.data.get('id')
        gamble = get_object_or_404(Gamble, id=gamble_id)
        if not gambler.gambles.filter(id=gamble_id).exists():
            return Response({"error": "You are not authorized to delete this gamble"}, status=status.HTTP_403_FORBIDDEN)
        if gamble.fight_id:    
            self.update_gambler_account(gambler, gamble.bet_amount)  # Refund the amount
        gambler.gambles.remove(gamble)
        gamble.delete()
        return Response(f'Gamble {request.data.get("id")} has been deleted', status=status.HTTP_200_OK)
    

def manage_all_fight_gambles(fight_id):
    """
    Function to manage gambles after a fight is over.
    """
    fight = get_object_or_404(Fight, id=fight_id)
    for gamble in Gamble.objects.filter(fight_id=fight):
        manage_gamble(gamble, fight.winner)


def manage_gamble(gamble, fight_winner):
    """
    Function to manage an individual gamble after a fight is over.
    """
    gambler = gamble.gambler_set.first()
    if gambler: 
        gambler.gambles.remove(gamble)
        if gamble.assumed_winner:
            if gamble.assumed_winner == fight_winner:
                amount_won = gamble.bet_amount * fight_winner.rank
                gambler.account_balance += amount_won
                gambler.save()
        else:
            # If fight was deleted, refund the money
            gambler.account_balance += gamble.bet_amount
            gambler.save()


