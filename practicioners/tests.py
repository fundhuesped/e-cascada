from rest_framework.test import APITestCase
from practicioners.models import AvailableTime, Characteristic, Eligibility, ReferralMethod, ServiceCategory, ServiceProvisioningCode, Speciality, TypeService
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

class CharacteristicTest(APITestCase):
    def test_createCharacteristic(self):
        """
        Asegura crear un Characteristic(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba'}
        response = self.client.post('/practicioners/characteristic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getCharacteristics(self):
        """
        Obtiene todas las Characteristic(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createCharacteristic()
        response = self.client.get('/practicioners/characteristic/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getCharacteristic(self):
        """
        Obtiene una Characteristic(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createCharacteristic()
        response = self.client.get('/practicioners/characteristic/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteCharacteristic(self):
        """
        Elinima un Characteristic
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createCharacteristic()
        response = self.client.delete('/practicioners/characteristic/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Characteristic.objects.count(),0)

    def test_updateCharacteristic(self):
        """
        Modifica un Characteristic
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createCharacteristic()
        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba 2'}
        response = self.client.put('/practicioners/characteristic/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['text'],'Prueba 2')

class EligibilityTest(APITestCase):
    def test_createEligibility(self):
        """
        Asegura crear un Eligibility(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba'}
        response = self.client.post('/practicioners/eligibility/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getEligibilities(self):
        """
        Obtiene todas las Eligibility(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createEligibility()
        response = self.client.get('/practicioners/eligibility/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getEligibility(self):
        """
        Obtiene una Eligibility(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createEligibility()
        response = self.client.get('/practicioners/eligibility/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteEligibility(self):
        """
        Elinima un Eligibility
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createEligibility()
        response = self.client.delete('/practicioners/eligibility/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Eligibility.objects.count(),0)

    def test_updateEligibility(self):
        """
        Modifica un Eligibility
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createEligibility()
        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba 2'}
        response = self.client.put('/practicioners/eligibility/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['text'],'Prueba 2')

class ReferralMethodTest(APITestCase):
    def test_createReferralMethod(self):
        """
        Asegura crear un ReferralMethod(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba'}
        response = self.client.post('/practicioners/referral-method/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getReferralMethods(self):
        """
        Obtiene todas las ReferralMethod(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createReferralMethod()
        response = self.client.get('/practicioners/referral-method/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getReferralMethod(self):
        """
        Obtiene una ReferralMethod(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createReferralMethod()
        response = self.client.get('/practicioners/referral-method/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteReferralMethod(self):
        """
        Elinima un ReferralMethod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createReferralMethod()
        response = self.client.delete('/practicioners/referral-method/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ReferralMethod.objects.count(),0)

    def test_updateReferralMethod(self):
        """
        Modifica un ReferralMethod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createReferralMethod()
        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba 2'}
        response = self.client.put('/practicioners/referral-method/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['text'],'Prueba 2')

class ServiceCategoryTest(APITestCase):
    def test_createServiceCategory(self):
        """
        Asegura crear un ServiceCategory(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba'}
        response = self.client.post('/practicioners/service-category/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getServiceCategories(self):
        """
        Obtiene todas las ServiceCategory(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceCategory()
        response = self.client.get('/practicioners/service-category/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getServiceCategory(self):
        """
        Obtiene una ServiceCategory(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceCategory()
        response = self.client.get('/practicioners/service-category/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteServiceCategory(self):
        """
        Elinima un ServiceCategory
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceCategory()
        response = self.client.delete('/practicioners/service-category/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ServiceCategory.objects.count(),0)

    def test_updateServiceCategory(self):
        """
        Modifica un ServiceCategory
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceCategory()
        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba 2'}
        response = self.client.put('/practicioners/service-category/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['text'],'Prueba 2')

class ServiceProvisioningCodeTest(APITestCase):
    def test_createServiceProvisioningCode(self):
        """
        Asegura crear un ServiceProvisioningCode(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba'}
        response = self.client.post('/practicioners/service-provisioning-code/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getServiceProvisioningCodes(self):
        """
        Obtiene todas las ServiceProvisioningCode(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceProvisioningCode()
        response = self.client.get('/practicioners/service-provisioning-code/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getServiceProvisioningCode(self):
        """
        Obtiene una ServiceProvisioningCode(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceProvisioningCode()
        response = self.client.get('/practicioners/service-provisioning-code/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteServiceProvisioningCode(self):
        """
        Elinima un ServiceProvisioningCode
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceProvisioningCode()
        response = self.client.delete('/practicioners/service-provisioning-code/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ServiceProvisioningCode.objects.count(),0)

    def test_updateServiceProvisioningCode(self):
        """
        Modifica un ServiceProvisioningCode
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceProvisioningCode()
        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba 2'}
        response = self.client.put('/practicioners/service-provisioning-code/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['text'],'Prueba 2')

class SpecialityTest(APITestCase):
    def test_createSpeciality(self):
        """
        Asegura crear un Speciality(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba'}
        response = self.client.post('/practicioners/speciality/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getSpecialities(self):
        """
        Obtiene todas las Speciality(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createSpeciality()
        response = self.client.get('/practicioners/speciality/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getSpeciality(self):
        """
        Obtiene una Speciality(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createSpeciality()
        response = self.client.get('/practicioners/speciality/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteSpeciality(self):
        """
        Elinima un Speciality
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createSpeciality()
        response = self.client.delete('/practicioners/speciality/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Speciality.objects.count(),0)

    def test_updateSpeciality(self):
        """
        Modifica un Speciality
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createSpeciality()
        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba 2'}
        response = self.client.put('/practicioners/speciality/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['text'],'Prueba 2')

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

    def createCharacteristic(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        characteristic = Characteristic.objects.create(
            coding = coding,
            text = "Characteristic"
        )
        return characteristic

    def createEligibility(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        eligibility = Eligibility.objects.create(
            coding = coding,
            text = "Eligibility"
        )
        return eligibility

    def createReferralMethod(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        rmethod = ReferralMethod.objects.create(
            coding = coding,
            text = "ReferralMethod"
        )
        return rmethod

    def createServiceCategory(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        serviceCategory = ServiceCategory.objects.create(
            coding = coding,
            text = "ServiceCategory"
        )
        return serviceCategory

    def createServiceProvisioningCode(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        sprovcode = ServiceProvisioningCode.objects.create(
            coding = coding,
            text = "ServiceProvisioningCode"
        )
        return sprovcode

    def createSpeciality(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        spec = Speciality.objects.create(
            coding = coding,
            text = "Speciality"
        )
        return spec

    def createTypeService(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        tser = TypeService.objects.create(
            coding = coding,
            text = "TypeService"
        )
        return tser

# Create your tests here.
