from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from users.models import MyUser


SCORE_CHOICES = zip(range(2, 6), range(2, 6))


"""
Path where exams will be uploaded to
"""


def upload_exams(instance, filename):
    return f'exam/{instance.owner.username}/{filename}'


class Exam(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    remark = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=upload_exams, blank=True, null=False)

    def __str__(self):
        return f'{self.title} of {self.owner.username}'


"""
Path where exam's answers will be uploaded to
"""


def upload_answers(instance, filename):
    return f'answer/{instance.owner.username}/{filename}'


class AnswerExam(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    to_exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    remark = models.TextField()
    score = models.IntegerField(choices=SCORE_CHOICES, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=upload_answers, blank=True, null=False)

    def __str__(self):
        return f'{self.title}_answers of {self.owner.username}'

