from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from triangle.models import *
from triangle.serializers import *

class TriangleApiTestCase(APITestCase):
#     def test_get(self):
# #        url=reverse()                      #* функція для перетворення url-адрес

# #*      Тестування АРІ
#         employee_1=Employee.objects.create()          #* Для створення даних використовуються моделі
#         employee_2=Employee.objects.create()

#         response=self.client.get('')

#         serializer_data=EmployeeSerializer([employee_1,employee_2],many=True).data
#         self.assertEqual(serializer_data,response.data)

#         self.assertEqual(status.HTTP_200_OK,response.status_code)


    def test_employee_get(self):
        employee_1=Employee.objects.create(
            name="test employee 1",
            position="test",
            photo="/",
            facebook='facebook employee 1',
            twitter='twitter employee 1',
            email='employee_1@mail.com'
            )
        employee_2=Employee.objects.create(
            name="test employee 2",
            position="test",
            photo="/",
            facebook='facebook_employee_2',
            twitter='twitter_employee_2',
            email='employee_2@mail.com'
        )

        response=self.client.get('api/v1/employee')
        
        print()
        print(response.content)
        print()

        # serializer_data=EmployeeSerializer([employee_1,employee_2],many=True).data
        self.assertEqual(3,len(response.data['results']))

        self.assertEqual(status.HTTP_200_OK,response.status_code)
