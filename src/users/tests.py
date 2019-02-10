from django.test import TestCase
from users.models import MyUser


class MyUserTestCase(TestCase):
    def setUp(self):
        myuser = MyUser.objects.create(username='konrad', email='konrad@wp.pl')
        myuser.set_password('konrad')
        myuser.save()

    def test_created_user(self):
        qs = MyUser.objects.filter(username='konrad')
        self.assertEqual(qs.count(), 1)
