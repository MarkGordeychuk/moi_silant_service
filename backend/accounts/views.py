from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import UserSerializer


class AuthView(APIView):
    def get(self, request, **kwargs):
        user = request.user
        if user.is_authenticated:
            serialized_user = UserSerializer(request.user)
            return Response({'auth': True, 'user': serialized_user.data})
        return Response({'auth': False})

    def post(self, request, **kwargs):
        username = request.data.get('name')
        user = authenticate(username=username, password=request.data.get('password'))
        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            serialized_user = UserSerializer(user)
            return Response({'auth': True, 'user': serialized_user.data, 'token': token.key})
        return Response({'auth': False})
