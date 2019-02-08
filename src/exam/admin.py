from django.contrib import admin
from .models import Exam, AnswerExam


class ExamAdmin(admin.ModelAdmin):
    list_filter = ['updated', 'timestamp']
    readonly_fields = ['updated', 'timestamp']
    list_display = ['title', 'owner', 'timestamp']
    search_fields = ['title', 'owner']

    class Meta:
        model = Exam


class AnswerExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']


admin.site.register(Exam, ExamAdmin)
admin.site.register(AnswerExam)
