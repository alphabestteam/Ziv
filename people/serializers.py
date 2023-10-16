from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "name",
            "id",
            "birth_date",
            "city",
        ]

    def create(self, validated_data):
        return Person(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.id = validated_data.get("id", instance.id)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.city = validated_data.get("city", instance.city)
        return instance
