from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Applicant(models.Model):
    name = models.CharField(max_length=10)
    group = models.ForeignKey('auth.Group', on_delete=models.CASCADE, default=None)
    email = models.EmailField(default="")
    phone = models.CharField(max_length=11, default="")
    birthday = models.DateField(default=timezone.localdate)
    timestamp = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.name

    def get_applicant_application(self):
        return self.applicantapplication_set.only('application')

    def get_applicant_application_count(self):
        return self.get_applicant_application().count()


class Application(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.name

    def get_application_applicant(self):
        return self.applicantapplication_set.all()

    def get_application_applicant_count(self):
        return self.get_application_applicant().count()


class Question(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    question = models.CharField(max_length=150)
    timestamp = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.question


class Answer(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return self.answer


class ApplicantApplication(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self):
        return "%s님의 %s" % (self.applicant, self.application)

    def get_application_name(self):
        return self.application.name

    def get_application_timestamp(self):
        return self.application.timestamp

    def get_applicant(self):
        return self.applicant

    def get_application_data(self):
        questions = self.application.question_set.all().order_by('order')
        answers = list()
        for question in questions:
            try:
                answer = Answer.objects.get(applicant=self.applicant, question=question)
            except Answer.DoesNotExist:
                answer = None
            answers.append((question, answer))
        return answers


class Evaluation(models.Model):
    application = models.ForeignKey(ApplicantApplication, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.localtime)


class AnswerEvaluation(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.localtime)
