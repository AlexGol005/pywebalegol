from rest_framework import serializers
from blog.models import Note, Comment

def note_to_json(note):
    return {
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "create_at": note.create_at,
        "update_at": note.update_at,
    }

def note_created(note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "create_at": note.create_at,
        "update_at": note.update_at,
    }

class NoteSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ("author", ) #при передаче извне это поле будет проигнорировано

class PublicNoteSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ("author", )

class CommentSerializer(serializers.ModelSerializer):
    # todo serializers.SerializerMethodField
    # rating = serializers.SerializerMethodField('get_rating')
    #
    # def get_rating(self, obj):
    #     return {
    #         'value': obj.rating,
    #         'display': obj.get_rating_display()
    #     }

    class Meta:
        model = Comment
        fields = "__all__"


class AuthorNoteSerialiser(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = (
            'title', 'message', 'create_at', 'update_at',  # из модели
            'author', 'comments',  # из сериализатора
        )
        read_only_fields = ("author", )