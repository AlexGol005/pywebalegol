from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from blog.models import Note
from . import serializers


class NoteListCreateApiView(APIView):
    # def get(self, request):
    #     objects = Note.objects.all()
    #     return Response(serializers.note_to_json(obj) for obj in objects)
    def get(self, request):
        notes = Note.objects.all()
        serializer = serializers.NoteSerialiser(
            instance=notes,
            many=True,

        )
        return Response(serializer.data)

    def post(self, request: Request):
        #data = request.data #данные получены из реквеста типа инпут
        #note = Note(**data)
        #note.save(force_insert=True)

        # return Response(
        #     serializers.note_created(note),
        #     status=status.HTTP_201_CREATED
        # )
        serializer = serializers.NoteSerialiser(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(
            serializer.data
        )

class NoteDetailAPIView(APIView):
    """ Представление, которое позволяет вывести отдельную запись. """
    def get(self, request, pk):  # todo path param
        # note = Note.objects.get(pk=pk)
        notes = get_object_or_404(Note, pk=pk)


        return Response(serializers.note_to_json(notes))

    def put(self, request: Request, pk):
        data = request.data
        note = Note.objects.get(pk=pk)
        note.title = data["title"]
        note.message = data["message"]
        note.save()
        return Response(
            serializers.note_created(note),
            status=status.HTTP_200_OK
        )

# class NotePublicNoteListAPIView(ListAPIView):
#     queryset = Note.objects.all()
#     serializer_class = serializers.NoteSerialiser
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(public=True)

class NotePublicNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.AuthorNoteSerialiser

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)
