from django.contrib import admin

from assignment.models import Assignment, Submit, Question, Answer, SubmitImage, AssignmentSubmitInformation

# Register your models here.

admin.site.register(Assignment)
admin.site.register(AssignmentSubmitInformation)
admin.site.register(Submit)
admin.site.register(SubmitImage)
admin.site.register(Question)
admin.site.register(Answer)
