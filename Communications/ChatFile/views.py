from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import ChatFile
from User.models import User
from User.views import clear_inbox
from .serializers import ChatFileSerializer
from Message.serializers import MessageSerializer
from Message.models import Message
from File.views import FileView
from File.views import add_collaborator
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ChatFileView(APIView):
    def post(self, request):
        serialized_chat_file = ChatFileSerializer(data=request.data)
        if serialized_chat_file.is_valid():
            serialized_chat_file.save()
            return Response(serialized_chat_file.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, file_id):
        user = get_object_or_404(User, id=user_id)
        chat_file = get_object_or_404(ChatFile, id=file_id)
        if user == chat_file.creator or user in chat_file.collaborators.all():
            serializer = ChatFileSerializer(chat_file, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(f"User number {user_id} does not have access to this chat file", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id, file_id):
        user = get_object_or_404(User, id=user_id)
        chat_file = get_object_or_404(ChatFile, id=file_id)
        if user == chat_file.creator or user in chat_file.collaborators.all():
            chat_messages = chat_file.messages.all()
            unread_messages = user.unread_messages.all()
            for message in chat_messages:
                if message in unread_messages:
                    user.unread_messages.remove(message)
            user.save()
            serialized_file = ChatFileSerializer(chat_file)
            return Response(serialized_file.data, status=status.HTTP_200_OK)
        return Response(f"User number {user_id} does not have access to this chat file", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, file_id):
        user = get_object_or_404(User, id=user_id)
        chat_file = get_object_or_404(ChatFile, id = file_id)
        if user == chat_file.creator or user in chat_file.collaborators.all():
            chat_file.delete()
            return Response(f"Chat file number {file_id} has been deleted", status=200)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)
    


@api_view(["GET"])
def chat_file_messages(request, file_id, user_id):
    """
    The function receives a GET request, a user id and a file id
    The functions gets the user and file
    If the user has access to the file, the function returns all the messages of this chat
    If they don't, a message is printed
    """
    user = get_object_or_404(User, id=user_id)
    chat_file = get_object_or_404(ChatFile, id=file_id)
    if user == chat_file.creator or user in chat_file.collaborators.all():
        messages = Message.objects.filter(chat_files=chat_file)
        serialized_messages = MessageSerializer(messages, many=True)
        return Response(serialized_messages.data, safe=False)
    else:
        return Response(f"User number {user_id} does not have access to this chat file", status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["PUT"])
def add_message(request, file_id):
    """
    The function receives a file id and a PUT request with a JSON
    The function access the request Chat file and checks the request data
    If the id belongs to the sender of the text and he belongs in the chat
    The message is added to the chat
    The message is also added to the inbox of all the recipients
    """
    chat_file = get_object_or_404(ChatFile, id=file_id)
    message = get_object_or_404(Message, id=request.data["message_id"])
    sender = get_object_or_404(User, id=request.data["sender_id"])
    if (sender == chat_file.creator or sender in chat_file.collaborators.all()) and sender == message.sender:
        chat_file.messages.add(message)
        for user in list(chat_file.collaborators.all()) + [chat_file.creator]:
                #Make sure to message isn't added to the inbox of the sender
                if user != message.sender:
                    user.unread_messages.add(message)
        return Response(f"Message number {request.data['message_id']} has been added to the chat", status=200)
    return Response(f"Admin number {request.data['sender_id']} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)


