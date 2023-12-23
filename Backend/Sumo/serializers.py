from rest_framework import serializers
from .models import Sumo

class SumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sumo
        fields ='__all__'

    def to_representation(self, instance):
        if isinstance(instance, int):
            # If instance is an ID, return a dictionary with the 'id' field
            return {'id': instance}
        elif isinstance(instance, dict):
            # If instance is already a dictionary, return it as is
            return instance
        return super().to_representation(instance)