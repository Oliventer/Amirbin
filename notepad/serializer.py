from rest_framework import serializers
from notepad.models import Note


class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['url', 'created', 'code', 'language', 'style']
