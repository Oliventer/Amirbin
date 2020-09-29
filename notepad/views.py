from rest_framework import viewsets, renderers, status
from notepad.models import Note
from notepad.serializer import NotesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import random
import string


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        note = self.get_object()
        return Response(note.highlighted)
