from django.contrib import admin

from assignment.models import Assignment, Submit, Question, Answer

# Register your models here.

admin.site.register(Assignment)
admin.site.register(Submit)
admin.site.register(Question)
admin.site.register(Answer)
