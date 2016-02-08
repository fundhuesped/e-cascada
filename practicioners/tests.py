from rest_framework.test import APITestCase
from practicioners.models import AvailableTime
from common.tests import CommonTestHelper
from datetime import datetime
from rest_framework import status

class AvailableTimeTest(APITestCase):
    def test_createAvailableTime(self):
        """
        Asegura crear un AvailableTime(
        :return:
        """
        helper = CommonTestHelper()
        helper.createDayOfWeek()
        helper.createDayOfWeek()

        data= {'daysOfWeek': ['http://localhost:8000/common/day-of-week/1/','http://localhost:8000/common/day-of-week/2/'],'allDay': 'false','availableStartTime': '08:00:00','availableEndTime': '13:00:00'}
        response = self.client.post('/practicioners/available-time/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getAvailableTimes(self):
        """
        Obtiene todas las AvailableTime(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createAvailableTime()
        response = self.client.get('/practicioners/available-time/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAvailableTime(self):
        """
        Obtiene una AvailableTime(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createAvailableTime()
        response = self.client.get('/practicioners/available-time/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredAvailableTime(self):
        """
        Obtiene un AvailableTime filtrado
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createAvailableTime()
        response = self.client.get('/practicioners/available-time/?allDay=False',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteAvailableTime(self):
        """
        Elinima un AvailableTime
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createAvailableTime()
        response = self.client.delete('/practicioners/available-time/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AvailableTime.objects.count(),0)

    def test_updateAvailableTime(self):
        """
        Modifica un AvailableTime
        :return:
        """
        helperc = CommonTestHelper()
        helperc.createDayOfWeek()
        helperp = PracticionerTestHelper()
        helperp.createAvailableTime()
        data= {'daysOfWeek': ['http://localhost:8000/common/day-of-week/2/'],'allDay': 'false','availableStartTime': '09:00:00','availableEndTime': '13:00:00'}
        response = self.client.put('/practicioners/available-time/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['availableStartTime'],'09:00:00')
        self.assertEqual(response.json()['daysOfWeek'][0],'http://testserver/common/day-of-week/2/')


class PracticionerTestHelper:
    def createAvailableTime(self):
        commonHelper = CommonTestHelper()
        dayOfWeek = commonHelper.createDayOfWeek()

        atime = AvailableTime.objects.create(
            allDay = False,
            availableStartTime = datetime.now().time(),
            availableEndTime = datetime.now().time(),
        )

        atime.daysOfWeek.add(dayOfWeek)
        atime.save()

        return dayOfWeek
# Create your tests here.
