from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        id = serializers.ReadOnlyField()
        fields = "__all__"
