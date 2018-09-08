from django.test import TestCase


# Create your tests here.


class HellTest(TestCase):

    def testHello(self):
        print('asdf')
        a = 3
        self.assertEqual(a, 3)
