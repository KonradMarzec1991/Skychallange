from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from users.models import MyUser
from exam.models import Exam, AnswerExam


class MyUserTestCase(APITestCase):

    def setUp(self):
        myuser_exam = MyUser.objects.create(username='lecturer', email='lecturer@wp.pl')
        myuser_exam.set_password('lecturer')
        myuser_exam.is_lecturer = True
        myuser_exam.save()

        exam = Exam.objects.create(title='exam', remark='no remarks', owner=myuser_exam)

    def test_created_user_exams(self):
        myusers = MyUser.objects.all()
        self.assertEqual(myusers.count(), 1)
        exams = Exam.objects.all()
        self.assertEqual(exams.count(), 1)
        exams = exams.filter(title='exam')
        self.assertEqual(exams.count(), 1)
        ans = AnswerExam.objects.all()
        self.assertEqual(ans.count(), 0)

    def test_requests(self):
        client = RequestsClient()
        response_detail = client.get('http://127.0.0.1:8000/api/exam/1/')
        assert response_detail.status_code == 200

        response_exam = client.get('http://127.0.0.1:8000/api/list_exam/')
        assert response_exam.status_code == 200

        response_answ = client.get('http://127.0.0.1:8000/api/list_answers/')
        assert response_answ.status_code == 200

    def test_reverse(self):
        id = 1
        exam_url = api_reverse('exams:exam-detail', kwargs={'id': id})
        response = self.client.get(exam_url, data=None, format='json')
        assert response.status_code == 200

    def test_put_get(self):
        myuser = MyUser.objects.get(id=1)
        exam = Exam.objects.create(title='EXAM10', owner=myuser, remark='no remarks')
        exams = Exam.objects.all()
        self.assertEqual(exams.count(), 2)

        client = RequestsClient()
        response_detail = client.get('http://127.0.0.1:8000/api/exam/1/')
        assert response_detail.status_code == 200

        response_detail = client.get('http://127.0.0.1:8000/api/exam/2/')
        assert response_detail.status_code == 200

        data = {
            'title': 'EXAM101',
            'owner': 1,
            'remark': 'remark1'
        }

        url = 'http://127.0.0.1:8000/api/exam/2/'

        """get method/retireve"""

        get_response = self.client.get(url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        """put / update"""

        put_response = self.client.put(url, data)
        new_data = put_response.data
        self.assertEqual(new_data['title'], data['title'])









