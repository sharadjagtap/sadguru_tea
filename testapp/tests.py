from django.test import TestCase

from testapp.models import Tea

class TeaTestCase(TestCase):
    def setUp(self):
        print("setUp activity")
        Tea.objects.create(name="Sadguru",description="It is very good",price=15)
        Tea.objects.create(name="Kadak_Chai",description="It is Kadak Chai",price=12)

    def test_tea_info(self):
        print("Testing Tea information")
        qs=Tea.objects.all()
        self.assertEqual(qs.count(),2)
        t1=Tea.objects.get(name="Sadguru")
        t2=Tea.objects.get(name="Kadak_Chai")
        self.assertEqual(t1.get_price(),15)
        self.assertEqual(t2.get_price(),12)

