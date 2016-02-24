from rest_framework.test import APITestCase
from practicioners.models import AvailableTime, Characteristic, Eligibility, HealthcareService, ReferralMethod, PracticionerQualificationPeriod, PracticionerRolePeriod, PracticionerRole, ServiceCategory, ServiceProvisioningCode, ServiceType, Speciality, TypeService, NotAvailable, NotAvailablePeriod, Role
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

class HealthCareServiceTest(APITestCase):
    def test_createHealthCareService(self):
        """
        Asegura crear un HealthCareService(
        :return:
        """
        commonHelper = CommonTestHelper()
        practHelper = PracticionerTestHelper()
        commonHelper.createIdentifier()
        commonHelper.createOrganization()
        practHelper.createServiceCategory()
        practHelper.createServiceType()
        commonHelper.createContactPoint()
        practHelper.createServiceProvisioningCode()
        practHelper.createCharacteristic()
        practHelper.createEligibility()
        practHelper.createReferralMethod()
        practHelper.createAvailableTime()
        practHelper.createNotAvailable()


        data= {
            'identifier': ['http://localhost:8000/common/identifier/1/'],
            'providedBy': 'http://localhost:8000/common/organization/1/',
            'serviceCategory': 'http://localhost:8000/practicioners/service-category/1/',
            'serviceType': ['http://localhost:8000/practicioners/service-type/1/'],
            'location':'Prueba',
            'serviceName':'Prueba',
            'comment':'Comentario',
            'extraDetails':'Detalles',
            'photo':'http://www.twitter.com/zentel',
            'telecom':['http://localhost:8000/common/contact-point/1/'],
            'coverageArea':'Location PRueba',
            'serviceProvisioningCode': ['http://localhost:8000/practicioners/service-provisioning-code/1/'],
            'eligibility':'http://localhost:8000/practicioners/eligibility/1/',
            'eligibilityNote':'Nota',
            'programName':'Nombre',
            'characteristic':['http://localhost:8000/practicioners/characteristic/1/'],
            'referralMethod':['http://localhost:8000/practicioners/referral-method/1/'],
            'publicKey':'Clave',
            'appointmentRequired':True,
            'availableTime':['http://localhost:8000/practicioners/available-time/1/'],
            'notAvailable':['http://localhost:8000/practicioners/not-available/1/'],
            'availabilityExceptions':'Nada'
        }
        response = self.client.post('/practicioners/healthcare-service/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getHealthCareServices(self):
        """
        Obtiene todas las ServiceType(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createHealthCareService()
        response = self.client.get('/practicioners/healthcare-service/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getHealthCareService(self):
        """
        Obtiene una ServiceType(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createHealthCareService()
        response = self.client.get('/practicioners/healthcare-service/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteHealthCareService(self):
        """
        Elinima un ServiceType
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createHealthCareService()
        response = self.client.delete('/practicioners/healthcare-service/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HealthcareService.objects.count(),0)

    def test_updateHealthCareService(self):
        """
        Modifica un ServiceType
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createHealthCareService()
        chelper = CommonTestHelper()
        chelper.createIdentifier()

        data= {
            'identifier': ['http://localhost:8000/common/identifier/1/', 'http://localhost:8000/common/identifier/2/'],
            'providedBy': 'http://localhost:8000/common/organization/1/',
            'serviceCategory': 'http://localhost:8000/practicioners/service-category/1/',
            'serviceType': ['http://localhost:8000/practicioners/service-type/1/'],
            'location':'Prueba 2',
            'serviceName':'Prueba',
            'comment':'Comentario',
            'extraDetails':'Detalles',
            'photo':'http://www.twitter.com/zentel',
            'telecom':['http://localhost:8000/common/contact-point/1/'],
            'coverageArea':'Location PRueba',
            'serviceProvisioningCode': ['http://localhost:8000/practicioners/service-provisioning-code/1/'],
            'eligibility':'http://localhost:8000/practicioners/eligibility/1/',
            'eligibilityNote':'Nota',
            'programName':'Nombre',
            'characteristic':['http://localhost:8000/practicioners/characteristic/1/'],
            'referralMethod':['http://localhost:8000/practicioners/referral-method/1/'],
            'publicKey':'Clave',
            'appointmentRequired':True,
            'availableTime':['http://localhost:8000/practicioners/available-time/1/'],
            'notAvailable':['http://localhost:8000/practicioners/not-available/1/'],
            'availabilityExceptions':'Nada'
        }
        response = self.client.put('/practicioners/healthcare-service/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['identifier'][1],'http://testserver/common/identifier/2/')
        self.assertEqual(response.json()['location'],'Prueba 2')

class NotAvailableTest(APITestCase):
    def test_createNotAvailable(self):
        """
        Asegura crear un NotAvailable(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailablePeriod()
        data= {'description': 'Not Available','during': 'http://localhost:8000/practicioners/not-available-period/1/'}
        response = self.client.post('/practicioners/not-available/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getNotAvailables(self):
        """
        Obtiene todas las NotAvailable(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailable()
        response = self.client.get('/practicioners/not-available/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getNotAvailable(self):
        """
        Obtiene una NotAvailable(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailable()
        response = self.client.get('/practicioners/not-available/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteNotAvailable(self):
        """
        Elinima un NotAvailable
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailable()
        response = self.client.delete('/practicioners/not-available/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NotAvailable.objects.count(),0)

    def test_updateNotAvailable(self):
        """
        Modifica un NotAvailable
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailable()
        helper.createNotAvailablePeriod()
        data= {'description': 'Not Available 2','during': 'http://localhost:8000/practicioners/not-available-period/2/'}
        response = self.client.put('/practicioners/not-available/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['description'],'Not Available 2')
        self.assertEqual(response.json()['during'],'http://testserver/practicioners/not-available-period/2/')

class NotAvailablePeriodTest(APITestCase):
    def test_createNotAvailablePeriod(self):
        """
        Asegura crear un NotAvailablePeriod(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'start': '2016-05-01T10:00:00','end': '2017-03-05T11:00:00'}
        response = self.client.post('/practicioners/not-available-period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getNotAvailablePeriods(self):
        """
        Obtiene todas las Eligibility(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailablePeriod()
        response = self.client.get('/practicioners/not-available-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getNotAvailablePeriod(self):
        """
        Obtiene una NotAvailablePeriod(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailablePeriod()
        response = self.client.get('/practicioners/not-available-period/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteNotAvailablePeriod(self):
        """
        Elinima un NotAvailablePeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailablePeriod()
        response = self.client.delete('/practicioners/not-available-period/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NotAvailablePeriod.objects.count(),0)

    def test_updateNotAvailablePeriod(self):
        """
        Modifica un NotAvailablePeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createNotAvailablePeriod()
        data= {'start': '2016-05-02T10:00:00','end': '2017-03-05T11:00:00'}
        response = self.client.put('/practicioners/not-available-period/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['start'],'2016-05-02T10:00:00')

class PracticionerRolePeriodTest(APITestCase):
    def test_createPracticionerRolePeriod(self):
        """
        Asegura crear un PracticionerRolePeriod(
        :return:
        """

        data= {'start': '2016-05-01T10:00:00','end': '2017-03-05T11:00:00'}
        response = self.client.post('/practicioners/practicioner-role-period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getPracticionerRolePeriods(self):
        """
        Obtiene todos los PracticionerRolePeriods
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRolePeriod()
        response = self.client.get('/practicioners/practicioner-role-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPracticionerRolePeriod(self):
        """
        Obtiene un PracticionerRolePeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRolePeriod()
        response = self.client.get('/practicioners/practicioner-role-period/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePracticionerRolePeriod(self):
        """
        Elinima un PracticionerRolePeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRolePeriod()
        response = self.client.delete('/practicioners/practicioner-role-period/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PracticionerRolePeriod.objects.count(),0)

    def test_updatePracticionerRolePeriod(self):
        """
        Modifica un PracticionerRolePeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRolePeriod()
        data= {'start': '2016-05-02T10:00:00','end': '2017-03-05T11:00:00'}
        response = self.client.put('/practicioners/practicioner-role-period/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['start'],'2016-05-02T10:00:00')

class PracticionerRoleTest(APITestCase):
    def test_createPracticionerRole(self):
        """
        Asegura crear un PracticionerRole
        :return:
        """
        helper = PracticionerTestHelper()
        chelper = CommonTestHelper()

        managingOrganization = chelper.createOrganization()
        role = helper.createRole()
        speciality = helper.createSpeciality()
        period = helper.createPracticionerRolePeriod()
        location = chelper.createLocation()
        healthCareService = helper.createHealthCareService()

        data = {
                "managingOrganization": "http://localhost:8000/common/organization/1/",
                "role": "http://localhost:8000/practicioners/role/1/",
                "speciality": [
                    "http://localhost:8000/practicioners/speciality/1/"
                ],
                "period": "http://localhost:8000/practicioners/practicioner-role-period/1/",
                "location": [
                    "http://localhost:8000/common/location/1/"
                ],
                "healthCareService": [
                    "http://localhost:8000/practicioners/healthcare-service/1/"
                ]
        }

        response = self.client.post('/practicioners/practicioner-role/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getPracticionerRoles(self):
        """
        Obtiene todos los PracticionerRole
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRole()
        response = self.client.get('/practicioners/practicioner-role/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPracticionerRole(self):
        """
        Obtiene un PracticionerRole
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRole()
        response = self.client.get('/practicioners/practicioner-role/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePracticionerRole(self):
        """
        Elinima un PracticionerRole
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRole()
        response = self.client.delete('/practicioners/practicioner-role/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PracticionerRole.objects.count(),0)

    def test_updatePracticionerRole(self):
        """
        Modifica un PracticionerRole
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerRole()
        helper.createSpeciality()
        helper.createRole()

        data = {
                "managingOrganization": "http://localhost:8000/common/organization/1/",
                "role": "http://localhost:8000/practicioners/role/2/",
                "speciality": [
                    "http://localhost:8000/practicioners/speciality/1/",
                    "http://localhost:8000/practicioners/speciality/2/"
                ],
                "period": "http://localhost:8000/practicioners/practicioner-role-period/1/",
                "location": [
                    "http://localhost:8000/common/location/1/"
                ],
                "healthCareService": [
                    "http://localhost:8000/practicioners/healthcare-service/1/"
                ]
        }

        response = self.client.put('/practicioners/practicioner-role/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['role'],'http://testserver/practicioners/role/2/')
        self.assertEqual(response.json()['speciality'][1],'http://testserver/practicioners/speciality/2/')

class PracticionerQualificationPeriodTest(APITestCase):
    def test_createPracticionerQualificationPeriod(self):
        """
        Asegura crear un PracticionerQualificationPeriod(
        :return:
        """

        data= {'start': '2016-05-01T10:00:00','end': '2017-03-05T11:00:00'}
        response = self.client.post('/practicioners/practicioner-qualification-period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getPracticionerQualificationPeriods(self):
        """
        Obtiene todos los PracticionerQualificationPeriods
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerQualificationPeriod()
        response = self.client.get('/practicioners/practicioner-qualification-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPracticionerQualificationPeriod(self):
        """
        Obtiene un PracticionerQualificationPeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerQualificationPeriod()
        response = self.client.get('/practicioners/practicioner-qualification-period/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePracticionerQualificationPeriod(self):
        """
        Elinima un PracticionerQualificationPeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerQualificationPeriod()
        response = self.client.delete('/practicioners/practicioner-qualification-period/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PracticionerQualificationPeriod.objects.count(),0)

    def test_updatePracticionerQualificationPeriod(self):
        """
        Modifica un PracticionerQualificationPeriod
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createPracticionerQualificationPeriod()
        data= {'start': '2016-05-02T10:00:00','end': '2017-03-05T11:00:00'}
        response = self.client.put('/practicioners/practicioner-qualification-period/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['start'],'2016-05-02T10:00:00')

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

class RoleTest(APITestCase):
    def test_createRole(self):
        """
        Asegura crear un Role(
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()

        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba'}
        response = self.client.post('/practicioners/role/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getRoles(self):
        """
        Obtiene todos los Role
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createRole()
        response = self.client.get('/practicioners/role/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getRole(self):
        """
        Obtiene un Role
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createRole()
        response = self.client.get('/practicioners/role/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteRole(self):
        """
        Elinima un Role
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createRole()
        response = self.client.delete('/practicioners/role/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Role.objects.count(),0)

    def test_updateEligibility(self):
        """
        Modifica un Eligibility
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createRole()
        data= {'coding': 'http://localhost:8000/common/coding/1/','text': 'Prueba 2'}
        response = self.client.put('/practicioners/role/1/', data, format='json')
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

class ServiceTypeTest(APITestCase):
    def test_createServiceType(self):
        """
        Asegura crear un ServiceType(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createTypeService()
        helper.createSpeciality()

        data= {'type': 'http://localhost:8000/practicioners/type-service/1/','speciality': 'http://localhost:8000/practicioners/speciality/1/'}
        response = self.client.post('/practicioners/service-type/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getServiceTypes(self):
        """
        Obtiene todas las ServiceType(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceType()
        response = self.client.get('/practicioners/service-type/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getServiceType(self):
        """
        Obtiene una ServiceType(
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceType()
        response = self.client.get('/practicioners/service-type/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteServiceType(self):
        """
        Elinima un ServiceType
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceType()
        response = self.client.delete('/practicioners/service-type/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ServiceType.objects.count(),0)

    def test_updateServiceType(self):
        """
        Modifica un ServiceType
        :return:
        """
        helper = PracticionerTestHelper()
        helper.createServiceType()
        helper.createTypeService()
        data= {'type': 'http://localhost:8000/practicioners/type-service/2/','speciality': 'http://localhost:8000/practicioners/speciality/1/'}
        response = self.client.put('/practicioners/service-type/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['type'],'http://testserver/practicioners/type-service/2/')

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

        return atime

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

    def createHealthCareService(self):
        commonHelper = CommonTestHelper()
        practHelper = PracticionerTestHelper()
        identifier = commonHelper.createIdentifier()
        providedBy = commonHelper.createOrganization()
        serviceCategory = practHelper.createServiceCategory()
        serviceType = practHelper.createServiceType()
        location = 'Location a cambiar'
        serviceName = 'Servicio de prueba'
        comment = None
        extraDetails = None
        photo = None
        telecom = commonHelper.createContactPoint()
        coverageArea = 'Location a cambiar'
        serviceProvisioningCode = practHelper.createServiceProvisioningCode()
        eligibility = practHelper.createEligibility()
        eligibilityNote = None
        programName = None
        characteristic = practHelper.createCharacteristic()
        referralMethod = practHelper.createReferralMethod()
        publicKey = None
        appointmentRequired = True
        availableTime = practHelper.createAvailableTime()
        notAvailable = practHelper.createNotAvailable()
        availabilityExceptions = None

        hcs = HealthcareService.objects.create(
            providedBy = providedBy,
            serviceCategory = serviceCategory,
            location = location,
            serviceName = serviceName,
            comment = comment,
            extraDetails = extraDetails,
            photo = photo,
            coverageArea = coverageArea,
            eligibility = eligibility,
            eligibilityNote = eligibilityNote,
            programName = programName,
            publicKey = publicKey,
            appointmentRequired = appointmentRequired,
            availabilityExceptions = availabilityExceptions
        )
        hcs.identifier.add(identifier)
        hcs.serviceType.add(serviceType)
        hcs.telecom.add(telecom)
        hcs.serviceProvisioningCode.add(serviceProvisioningCode)
        hcs.characteristic.add(characteristic)
        hcs.referralMethod.add(referralMethod)
        hcs.availableTime.add(availableTime)
        hcs.notAvailable.add(notAvailable)
        return hcs

    def createNotAvailable(self):
        nap = self.createNotAvailablePeriod()
        na = NotAvailable.objects.create(
            description = 'Not Available',
            during = nap
        )
        return na

    def createNotAvailablePeriod(self):
        nap = NotAvailablePeriod.objects.create(
            start = datetime.now(),
            end = datetime.now()
        )
        return nap

    def createPracticionerQualificationPeriod(self):
        pqp = PracticionerQualificationPeriod.objects.create(
            start = datetime.now(),
            end = datetime.now()
        )
        return pqp

    def createPracticionerRole(self):
        helper = PracticionerTestHelper()
        chelper = CommonTestHelper()

        managingOrganization = chelper.createOrganization()
        role = helper.createRole()
        speciality = helper.createSpeciality()
        period = helper.createPracticionerRolePeriod()
        location = chelper.createLocation()
        healthCareService = helper.createHealthCareService()

        pr = PracticionerRole.objects.create(
            managingOrganization = managingOrganization,
            role = role,
            period = period
        )
        pr.speciality.add(speciality)
        pr.location.add(location)
        pr.healthCareService.add(healthCareService)

        return pr


    def createPracticionerRolePeriod(self):
        nap = PracticionerRolePeriod.objects.create(
            start = datetime.now(),
            end = datetime.now()
        )
        return nap

    def createReferralMethod(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        rmethod = ReferralMethod.objects.create(
            coding = coding,
            text = "ReferralMethod"
        )
        return rmethod

    def createRole(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        rol = Role.objects.create(
            coding = coding,
            text = "Role"
        )
        return rol

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

    def createServiceType(self):
        helper = PracticionerTestHelper()
        type = helper.createTypeService()
        spec = helper.createSpeciality()
        stype = ServiceType.objects.create(
            type = type,
            speciality = spec
        )
        return stype

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
