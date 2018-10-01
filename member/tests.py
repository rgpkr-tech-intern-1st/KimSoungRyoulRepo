# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase

from member.models import AccountManager
from member.models.user_info import UserInfo


class TestCaseForAdmin(TestCase):
    def testOne(self):
        AccountManager.create_superuser(username='sky5367', email='KimSoungRyoul@gmail.com', name='soungryoul',
                                        password='1234')


class TestCaseForLearning(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('---더미데이터 생성---')
        cls.dummy_user = User.objects.create(username='sky5367', password='qwerty12345', is_superuser=False,
                                             email='soungryoul.kim@rgpkorea.co.kr')
        cls.dummy_user_info = UserInfo.objects.create(name='김성렬', phone_num='010-7237-6602',
                                                      owner_mileage_amount=3570, user=cls.dummy_user)

    def setUp(self):
        print('테스트 시작했다 ~')

    def tearDown(self):
        print('테스트 끝났다')

    # 테스트 마다 테이터가 rollback 되는가? : 안
    def test_0002_check_is_rollback(self):
        user = User.objects.get(username='sky5367')
        self.assertIsNotNone(user, msg='user 객체가 비어있습니다 ')

        # 회원 생성 후 회원정보 테이블과 연결

    def test_00001_create_user(self):
        self.assertEqual(User.objects.get(username='sky5367').userinfo.phone_num, '010-7237-6602')
