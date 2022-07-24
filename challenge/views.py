from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from challenge.api import views


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def main_view(request):
    
    if "username" not in request.GET and "password" not in request.GET:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    elif "username" not in request.GET:
        return Response({'error': 'Please provide username'},
                        status=HTTP_400_BAD_REQUEST)
    elif "password" not in request.GET:
        return Response({'error': 'Please provide password'},
                        status=HTTP_400_BAD_REQUEST)

    username = request.GET["username"]
    password = request.GET["password"]
    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    login(request, user)
    # return redirect('users/')
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)