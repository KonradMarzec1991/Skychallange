from django.conf.urls import url
from .views import (
    ExamUpload,
    ExamAnswersUpload,
    ExamAPIView,
    ExamAnswerAPIView,
    ExamAPIDetailView,
    AnswerExamAPIDetailView)

urlpatterns = [
    url(r'^upload_exam/$', ExamUpload.as_view(), name='exam-upload'),
    url(r'^upload_answer/$', ExamAnswersUpload.as_view(), name='answer-upload'),
    url(r'^list_exam/$', ExamAPIView.as_view(), name='exam-list'),
    url(r'^list_answers/$', ExamAnswerAPIView.as_view(), name='answer-list'),
    url(r'^exam/(?P<id>\d+)/', ExamAPIDetailView.as_view(), name='exam-detail'),
    url(r'^answer/(?P<id>\d+)/', AnswerExamAPIDetailView.as_view(), name='answer-detail'),
]