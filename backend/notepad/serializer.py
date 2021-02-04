from rest_framework import serializers
from notepad.models import Note


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['pk', 'created', 'code', 'delete_after_viewing', 'delete_time', 'language', 'style']
        read_only_fields = ['pk']


class UploadFilesSerializer(serializers.Serializer):
    file = serializers.FileField()
    delete_after_viewing = serializers.BooleanField(default=False)
