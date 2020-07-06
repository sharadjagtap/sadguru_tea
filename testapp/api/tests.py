
from rest_framework.test import APITestCase
from testapp.models import Tea

class TeaAPITestCase(APITestCase):
    def setUp(self):
        Tea.objects.create(name="Adrak_Chai",description="It is very healthy",price=20)

    def test_get_method(self):
        url='http://127.0.0.1:8000/api/teainfo/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=Tea.objects.filter(name="Adrak_Chai")
        self.assertEqual(qs.count(),1)
        print("GET method status code:",response.status_code)

    def test_post_method_success(self):
        url='http://127.0.0.1:8000/api/teainfo/'
        data={
            'name':"Zakas_Chai",
            'description': "Chai is Zakas",
            'price': 14
        }
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
        print("POST method status code for success:",response.status_code)


    def test_post_method_fail(self):
        url='http://127.0.0.1:8000/api/teainfo/'
        data={
            'name':"Zakas_Chai",
            'description': "Chai is Zakas",
        }
        response=self.client.post(url,data,format='json')
        print("POST method status code for fail:",response.status_code)
        self.assertEqual(response.status_code,400)

    def test_delete_method_success(self):
        url='http://127.0.0.1:8000/api/teainfo/1/'
        response=self.client.delete(url)
        print("DELETE method status code for success:",response.status_code)
        self.assertEqual(response.status_code,204)



