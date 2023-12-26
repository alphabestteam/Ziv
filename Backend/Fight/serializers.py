from rest_framework import serializers
from .models import Fight
from Sumo.models import Sumo


class FightSerializer(serializers.ModelSerializer):
    challenging_sumo = serializers.PrimaryKeyRelatedField(queryset=Sumo.objects.all())
    opponent_sumo = serializers.PrimaryKeyRelatedField(queryset=Sumo.objects.all())

    challenger_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        source='challenging_sumo'
    )
    opponent_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        source='opponent_sumo'
    )

    winner_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        source='winner'
    )

    class Meta:
        model = Fight
        fields = ['challenging_sumo', 'opponent_sumo', 'date', 'fight_rank', 'winner', 'challenger_name', 'opponent_name', 'winner_name', 'id']
        

    def to_representation(self, instance):
        if isinstance(instance, int):
            # If instance is an ID, return a dictionary with the 'id' field
            return {'id': instance}
        elif isinstance(instance, dict):
            # If instance is already a dictionary, return it as is
            return instance
        return super().to_representation(instance)
        
    def create(self, validated_data):
        challenging_sumo = validated_data.pop('challenging_sumo')
        opponent_sumo = validated_data.pop('opponent_sumo')
        fight = Fight(**validated_data, challenging_sumo=challenging_sumo, opponent_sumo=opponent_sumo, winner=None)
        fight.save()
        return self.to_representation(fight)

