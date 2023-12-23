from rest_framework import serializers
from Gamble.models import Gamble
from Sumo.models import Sumo
from Fight.models import Fight

class GambleSerializer(serializers.ModelSerializer):
    fight_id = serializers.PrimaryKeyRelatedField(queryset=Fight.objects.all())
    assumed_winner = serializers.PrimaryKeyRelatedField(queryset=Sumo.objects.all())
    winner_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        source='assumed_winner'
    )
    class Meta:
        model = Gamble
        fields = ['fight_id', 'assumed_winner', 'bet_amount', 'winner_name', 'id']
