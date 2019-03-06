from django.contrib import admin

from recruitment.models import Applicant, Application, Question, Answer, ApplicantApplication, Evaluation

# Register your models here.

admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ApplicantApplication)
admin.site.register(Evaluation)
