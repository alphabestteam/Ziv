from rest_framework import serializers
from Gambler.models import Gambler
from Gamble.serializers import GambleSerializer 

class GamblerSerializer(serializers.ModelSerializer):
    gambles = GambleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Gambler
        fields = ['first_name', 'last_name', 'birthdate', 'account_balance', 
                'password', 'username', 'is_staff', 'gambles']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
