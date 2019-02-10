from django.test import TestCase
from users.models import MyUser
from .models import AnswerExam, Exam


class MyUserTestCase(TestCase):

    def setUp(self):
        myuser = MyUser.objects.create(username='student', email='student@wp.pl')
        myuser.set_password('isstudent')
        myuser.save()

        myuser_exam = MyUser.objects.create(username='lecturer', email='lecturer@wp.pl')
        myuser_exam.set_password('lecturer')
        myuser_exam.is_lecturer = True
        myuser_exam.save()

    def test_created_user_exams(self):
        myuser = MyUser.objects.get(username='student')
        lecturer = MyUser.objects.get(username='lecturer')
        exam = Exam.objects.create(title='exam', owner=lecturer, remark='no remarks')
        self.assertEqual(exam.id, 1)
        qs = Exam.objects.all()
        self.assertEqual(qs.count(), 1)

        ans = AnswerExam.objects.create(owner=myuser, title='answer', to_exam=exam)
        self.assertEqual(ans.id, 1)
        qs_answer = AnswerExam.objects.all()
        self.assertEqual(qs_answer.count(), 1)

