from rest_framework import status
from .models import File
from User.models import User
from .serializers import FileSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse


class FileView(APIView):

    def post(self, request):
        serialized_file = FileSerializer(data=request.data)
        if serialized_file.is_valid():
            serialized_file.save()
            return Response(serialized_file.data, status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id, file_id):
        user = get_object_or_404(User, id=user_id)
        file = get_object_or_404(File, id = file_id)
        if user == file.creator or user in file.collaborators.all():
            serialized_file = FileSerializer(file)
            return Response(serialized_file.data, status=status.HTTP_200_OK)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, user_id, file_id):
        user = get_object_or_404(User, id=user_id)
        file = get_object_or_404(File, id = file_id)
        if user == file.creator or user in file.collaborators.all():
            serializer = FileSerializer(file, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id, file_id):
        user = get_object_or_404(User, id=user_id)
        file = get_object_or_404(File, id = file_id)
        if user == file.creator or user in file.collaborators.all():
            file.delete()
            return Response(f"File number {file_id} has been deleted", status=200)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def add_collaborator(request, file_id):
    """
    The function receives a PUT request with a JSON body and file id
    The functions gets the admin (based on the JSON) and file
    If the admin is not the file's creator, the function adds the user_id to the collaborators
    If they aren't the admin, a message is printed
    """
    file = get_object_or_404(File, id = file_id)
    admin = get_object_or_404(User, id=request.data['admin_id'])
    if admin == file.creator:
        collaborator = get_object_or_404(User, id=request.data['collaborator_id'])
        file.collaborators.add(collaborator)
        return Response(f"Collaborator number {request.data['collaborator_id']} has been added to the file", status=200)
    return Response(f"Admin number {request.data['admin_id']} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)





