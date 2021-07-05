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


class PasswordlessTokenView(APIView):
    def get(self, request, user_email):
        user = User.objects.filter(email = user_email).first()
        
        if user is None:
            return Response(data = {'No such user registred'}, status=status.HTTP_404_NOT_FOUND)
        
        token = PaswordlessToken.objects.create(user=user)
        send_mail.delay(user_email, "authentification", token.genetate_url())
        return Response(status=status.HTTP_200_OK)


class PaswordlessRegistrationView(APIView):
    def get(self, request, user_email):
        user = User.objects.filter(email = user_email).first()

        if user is not None:
            return Response(data = {'Already registred'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        user_to_register = User.objects.create(email=user_email)
        token = PaswordlessToken.objects.create(user=user_to_register)
        send_mail.delay(user_email, "registration", token.genetate_url())
        return Response(status=status.HTTP_201_CREATED)
            
            
class CheckPaswordlessTokenView(APIView):
    def get(self, request, token_id):
        paswordless_token = PaswordlessToken.objects.get(token_id=token_id)
        
        if paswordless_token is None:
            return Response(data = {'Token not found'}, status=status.HTTP_404_NOT_FOUND)
        
        token = Token.objects.create(user=paswordless_token.user)
        paswordless_token.mark_as_used()
        return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        
class PaswordlessTokenViewSet(ModelViewSet):
    queryset = PaswordlessToken.objects.all()
    serializer_class = PaswordlessTokenSerializer