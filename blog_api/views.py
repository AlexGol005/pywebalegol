from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status

from blog.models import Note
from . import serializers


class NoteListCreateApiView(APIView):
    def get(self, request):
        objects = Note.objects.all()
        return Response(serializers.note_to_json(obj) for obj in objects)

    def post(self, request: Request):
        data = request.data
        note = Note(**data)

        note.save(force_insert=True)

        return Response(
            serializers.note_created(note),
            status=status.HTTP_201_CREATED
        )