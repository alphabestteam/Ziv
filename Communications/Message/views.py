from rest_framework import status
from .models import Message
from User.models import User
from .serializers import MessageSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse

class MessageView(APIView):

    def updates_recipient(message):
        chat_file = message.chat_file
        creator = chat_file.creator
        collaborators = chat_file.collaborators.all()
        for user in list(collaborators) + [creator]:
            #Make sure to message isn't added to the inbox of the sender
            if user != message.sender:
                user.unread_messages.add(message)
        return Response({'Message was sent to inbox of all participants'})


    def post(self, request):
        serialized_message = MessageSerializer(data=request.data)
        if serialized_message.is_valid():
            message = serialized_message.save()
            if message.chat_file:
                chat = message.chat_file
                chat.messages.add(message)
                chat.save
                MessageView.updates_recipient(message)
            return Response(serialized_message.data, status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        messages = Message.objects.all()
        serialized_messages = MessageSerializer(messages, many=True)
        return Response(serialized_messages.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, message_id):
        user = get_object_or_404(User, id=user_id)
        message = get_object_or_404(Message, id = message_id)
        if user == message.sender:
            serializer = MessageSerializer(message, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, user_id, message_id):
        user = get_object_or_404(User, id=user_id)
        message = get_object_or_404(Message, id = message_id)
        if user == message.sender:
            message.delete()
            return Response(f"Message number {message_id} has been deleted", status=200)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)

