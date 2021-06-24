from tokens.models import PaswordlessToken
from rest_framework import serializers

class PaswordlessTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaswordlessToken
        fields = '__all__'