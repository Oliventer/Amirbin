from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from tokens.serializers import PaswordlessTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from tokens.tasks import send_mail
from users.models import User
from tokens.models import PaswordlessToken
from tokens.serializers import PaswordlessTokenSerializer
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import login
from django.shortcuts import get_object_or_404


class PasswordlessLoginView(APIView):
    def post(self, request, user_email):
        user = get_object_or_404(User, email=user_email)

        token = PaswordlessToken.objects.create(user=user)
        send_mail.delay(user_email, "login", token.genetate_url())
        return Response(status=status.HTTP_200_OK)


class PaswordlessRegistrationView(APIView):
    def post(self, request, user_email):
        if User.objects.filter(email=user_email).exists():
            return Response(data = {'Already registred'}, status=status.HTTP_403_FORBIDDEN)
        
        user_to_register = User.objects.create(email=user_email)
        token = PaswordlessToken.objects.create(user=user_to_register)
        send_mail.delay(user_email, "registration", token.genetate_url())
        return Response(status=status.HTTP_201_CREATED)
            
            
class CheckPaswordlessTokenView(APIView):
    def post(self, request, token_id):
        paswordless_token = PaswordlessToken.objects.get(token_id=token_id)
        
        if paswordless_token is None:
            return Response(data = {'Token not found'}, status=status.HTTP_404_NOT_FOUND)
        
        token = Token.objects.create(user=paswordless_token.user)
        login(request, paswordless_token.user)
        paswordless_token.mark_as_used()
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        
        
class PaswordlessTokenViewSet(ModelViewSet):
    queryset = PaswordlessToken.objects.all()
    serializer_class = PaswordlessTokenSerializer