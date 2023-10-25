from rest_framework import status
from .models import Record
from .serializers import RecordSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from User.models import User
from File.views import add_collaborator



class RecordView(APIView):

    def post(self, request):
        serialized_record = RecordSerializer(data=request.data)
        if serialized_record.is_valid():
            serialized_record.save()
            return Response(serialized_record.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_record.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id, record_id):
        #Only users with access can view this file
        user = get_object_or_404(User, id=user_id)
        record = get_object_or_404(Record, id = record_id)
        if user == record.creator or user in record.collaborators.all():
            serialized_record = RecordSerializer(record)
            return Response(serialized_record.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, record_id):
        user = get_object_or_404(User, id=user_id)
        record = get_object_or_404(Record, id = record_id)
        if user == record.creator or user in record.collaborators.all():
            serializer = RecordSerializer(record, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id, record_id):
        user = get_object_or_404(User, id=user_id)
        record = get_object_or_404(Record, id = record_id)
        if user == record.creator or user in record.collaborators.all():
            record.delete()
            return Response(f"File number {record_id} has been deleted", status=200)
        return Response(f"User number {user_id} does not have access to this file", status=status.HTTP_400_BAD_REQUEST)



