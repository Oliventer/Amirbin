from rest_framework.views import APIView
from tokens.serializers import PaswordlessTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from tokens.tasks import send_mail
from users.models import User
from tokens.models import PaswordlessToken

class PasswordlessTokenView(APIView):
    def get(self, request, user_email, format=None):
        user = User.objects.filter(email = user_email).first()
        if user is None:
            return Response(data={'No such user registred'}, status=status.HTTP_404_NOT_FOUND)
        
        token = PaswordlessToken.objects.create(user=user)
        send_mail.delay(user_email, "authentification", token.genetate_url())
        return Response(status=status.HTTP_200_OK)
