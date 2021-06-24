from rest_framework.views import APIView
from tokens.serializers import PaswordlessTokenSerializer
from rest_framework.response import Response
from rest_framework import status

class PasswordlessTokenView(APIView):
    def get(self, request, user_email, format=None):
        return Response(data={'user_email': user_email}, status=status.HTTP_200_OK)
