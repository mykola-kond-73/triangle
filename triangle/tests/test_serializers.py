from django.test import TestCase
from triangle.serializers import *
from triangle.models import *

class TriangleSerializersTestCase(TestCase):
    def test_employee_serializer(self):
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

        data=EmployeeSerializer([employee_1,employee_2],many=True).data


        expected_data=[                             #* Дані які очікуємо тримати (такі самі як при створенні вище)
            {
                'name':"test employee 1",
                'position':"test",
                'photo':"/",
                'facebook':'facebook employee 1',
                'twitter':'twitter employee 1',
                'email':'employee_1@mail.com'
            },
            {
                'name':"test employee 2",
                'position':"test",
                'photo':"/",
                'facebook':'facebook_employee_2',
                'twitter':'twitter_employee_2',
                'email':'employee_2@mail.com'
            }   
        ]

        self.assertEqual(expected_data,data['results'])
