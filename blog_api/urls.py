from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('note/', views.NoteListCreateApiView.as_view()),
    path('note/<int:pk>', views.NoteDetailAPIView.as_view()),
]
