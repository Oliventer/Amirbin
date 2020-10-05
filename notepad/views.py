from rest_framework import viewsets, renderers, status
from notepad.models import Note
from notepad.serializer import NotesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().filter(created__range=[datetime.now() - timedelta(days=30), datetime.now()])
    serializer_class = NotesSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        note = self.get_object()
        return Response(note.highlighted)
