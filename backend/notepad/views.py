from rest_framework import viewsets, status, mixins
from notepad.models import Note
from notepad.serializer import NotesSerializer, UploadFilesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import timedelta
from notepad.services import UploadService
from django.utils import timezone


class NoteViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = Note.objects.all().filter(created__gt=timezone.now() - timedelta(days=30))

    def get_serializer_class(self):
        if self.action == "upload":
            return UploadFilesSerializer
        return NotesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        serializer_data = serializer.data
        if instance.delete_after_viewing:
            instance.delete()

        return Response(serializer_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = UploadService(**serializer.data)()
        headers = self.get_success_headers(serializer.data)
        return Response({'pk': note.pk}, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["POST"])
    def upload(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uploaded_file = serializer.validated_data["file"]
        note_instance = UploadService.from_file(uploaded_file)()

        return Response({"pk": note_instance.pk}, status=status.HTTP_201_CREATED)
