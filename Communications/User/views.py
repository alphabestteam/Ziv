from rest_framework import status
from .models import User
from .serializers import UserSerializer
from Message.serializers import MessageSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from Message.models import Message


class UserView(APIView):

    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, status=status.HTTP_201_CREATED)
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user_record = get_object_or_404(User, id=id)
        serialized_user = UserSerializer(user_record, data=request.data, partial=True)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = get_object_or_404(User, pk=id)
        user.delete()
        return Response(f"User number {id} has been deleted", status=200)

@api_view(["PUT"])
def clear_inbox(request, id):
    user_record = get_object_or_404(User, id=id)
    inbox = user_record.unread_messages.all()
    user_record.unread_messages.clear()
    serialized_messages = MessageSerializer(inbox, many=True)
    return Response(serialized_messages.data, status=status.HTTP_200_OK)

