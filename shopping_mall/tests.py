from django.test import TestCase


# Create your tests here.


class HelleTest(TestCase):

    def test_hello(self):
        print('asdf')
        a = 3
        self.assertEqual(a, 3)
