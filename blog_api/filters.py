def filter_notes_by_autor_id(queryset, author_id):
    return queryset.filter(author_id=author_id)