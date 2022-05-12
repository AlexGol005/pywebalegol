from django.contrib import admin
from .models  import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'message', 'public', 'create_at', 'update_at')
    fields = ('title', 'message', 'public', ('create_at', 'update_at'))

    readonly_fields = ('create_at', 'update_at')
    # разрешить редактирование
    # list_editable = ("is_available",)
    # Поиск по выбранным полям
    search_fields = ['title']
    list_filter = ['create_at', 'title']
