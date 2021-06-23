from rest_framework import viewsets
from users.serializers import UserSerializer
from users.models import User

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer