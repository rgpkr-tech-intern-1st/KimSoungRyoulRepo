# Create your tests here.
from django.test import TestCase

from orders.models.order import Order


class OrderTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('---더미데이터 생성---')

    def setUp(self):
        print('테스트 시작했다 ~')

    def tearDown(self):
        print('테스트 끝났다')

    def test_order(self):
        orders = Order.objects.all()
