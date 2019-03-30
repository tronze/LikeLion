from django.contrib import admin

from assignment.models import Assignment, Submit, Question, Answer, SubmitImage, AssignmentSubmitTotal, \
    AssignmentComment

# Register your models here.

admin.site.register(Assignment)
admin.site.register(AssignmentSubmitTotal)
admin.site.register(Submit)
admin.site.register(SubmitImage)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AssignmentComment)
