from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Gambler
from .serializers import GamblerSerializer
import jwt, datetime
from .decorators import get_gambler_from_token


class Register(APIView):
    def post(self, request):
        serialized_gambler = GamblerSerializer(data=request.data)
        if serialized_gambler.is_valid():
            serialized_gambler.save()
            return Response({'error':serialized_gambler.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serialized_gambler.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            gambler = Gambler.objects.filter(username=username).first()
        except Gambler.DoesNotExist:
            return Response('User not found', status=401)

        if not gambler.check_password(password):
            return Response('Incorrect Password', status=401)
        
        payload ={
            'id': gambler.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=180),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        print(token)
        response = Response()
        response.set_cookie(key='jwt', value = token, httponly=True)
        response.data = {'jwt': token}
        return response

class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = 'Successfully logged out'
        return response

class GamblerProfile(APIView):

    @get_gambler_from_token
    def get(self, request):
        serialized_gambler = GamblerSerializer(self.gambler)
        return Response(serialized_gambler.data, status=status.HTTP_200_OK)

class GamblerView(APIView):

    @get_gambler_from_token
    def put(self, request):
        serialized_gambler = GamblerSerializer(self.gambler, data=request.data, partial=True)
        if serialized_gambler.is_valid():
            serialized_gambler.save()
            return Response(serialized_gambler.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_gambler.errors, status=status.HTTP_400_BAD_REQUEST)

    @get_gambler_from_token
    def delete(self, request):
        self.gambler.delete()
        response = Response()
        response.delete_cookie('jwt')
        response.data = "Gambler has been deleted"
        return response