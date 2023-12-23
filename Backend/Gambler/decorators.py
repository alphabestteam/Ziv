# from functools import wraps
# from rest_framework.response import Response
# from rest_framework import status
# import jwt
# from .models import Gambler

# def get_gambler_from_token(view_func):
#     @wraps(view_func)
#     def _wrapped_view(self, request, *args, **kwargs):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             return Response("Token not provided.", status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#             gambler = Gambler.objects.get(id=payload['id'])
#             setattr(self, 'gambler', gambler)  # Attach the gambler to the instance for later use
#         except jwt.ExpiredSignatureError:
#             return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
#         except jwt.DecodeError:
#             return Response("Invalid token", status=status.HTTP_401_UNAUTHORIZED)
#         except Gambler.DoesNotExist:
#             return Response("Gambler not found", status=status.HTTP_404_NOT_FOUND)

#         return view_func(self, request, *args, **kwargs)

#     return _wrapped_view
from functools import wraps
from rest_framework.response import Response
from rest_framework import status
import jwt
from .models import Gambler

def get_gambler_from_token(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        token = request.COOKIES.get('jwt') or request.headers.get('Authorization', '').split('Bearer ')[-1]

        if not token:
            return Response("Token not provided.", status=status.HTTP_401_UNAUTHORIZED)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            gambler = Gambler.objects.get(id=payload['id'])
            setattr(self, 'gambler', gambler)  # Attach the gambler to the instance for later use
        except jwt.ExpiredSignatureError:
            return Response("Unauthenticated", status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            return Response("Invalid token", status=status.HTTP_401_UNAUTHORIZED)
        except Gambler.DoesNotExist:
            return Response("Gambler not found", status=status.HTTP_404_NOT_FOUND)

        return view_func(self, request, *args, **kwargs)

    return _wrapped_view
