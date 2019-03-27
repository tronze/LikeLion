from django.conf import settings
from django.db import models
from django.utils import timezone

from LikeLion import utils
from board.models import Post, Comment


# Create your models here.


class Assignment(models.Model):
    name = models.CharField(max_length=300)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    open = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True)
    materials = models.FileField(upload_to=utils.custom_path, blank=True)
    timestamp = models.DateTimeField(default=timezone.localtime)


class Submit(Post):
    languages = (
        (1, 'HTML'),
        (2, 'CSS'),
        (3, 'Python'),
        (4, '일반 텍스트'),
        (5, '링크'),
    )
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    language = models.PositiveSmallIntegerField(choices=languages)

    def __str__(self):
        return "%s - %s" % (self.title, self.author)


class AssignmentSubmitTotal(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=utils.custom_path)
    link = models.URLField()
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)


class SubmitImage(Submit):
    image = models.ImageField(upload_to=utils.custom_path)


class Question(Post):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    answered = models.BooleanField(default=False)


class Answer(Comment):
    accepted = models.BooleanField(default=False)
