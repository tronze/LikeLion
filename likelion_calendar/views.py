from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
from likelion_calendar.models import Comment


class CommentView(CreateView):
    model = Comment
    fields = ('post', 'author', 'content')
