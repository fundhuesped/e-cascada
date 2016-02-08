import json
from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from common.models import DayOfWeek, Coding, IdentifierType, IdentifierPeriod, ContactPointPeriod, AddressPointPeriod, NamePeriod, AddressLine, ContactPoint, Address, HumanName, OrganizationContact, Identifier

class CodingTest(APITestCase):
    def test_createCoding(self):
        """
        Asegura que el Coding se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'system': 'http://foo.test', 'version': '1.0', 'code': 'TES', 'display': 'TESTING','userSelected': 'false'}
        cantCodings = Coding.objects.count()
        response = self.client.post('/common/coding/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(Coding.objects.count(),cantCodings)

    def test_getCodings(self):
        """
        Asegura obtener Codings
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createCoding()
        response = self.client.get('/common/coding/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getCoding(self):
        """
        Asegura obtener un Coding
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createCoding()
        response = self.client.get('/common/coding/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getCodingFiltered(self):
        """
        Asegura obtener un Coding con filtro
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createCoding()
        response = self.client.get('/common/coding/?code=TES&display=TESTING',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_deleteCoding(self):
        """
        Asegura que se puedan eliminar Codings
        :return:
        """
        helper = CommonTestHelper()
        helper.createCoding()
        response = self.client.delete('/common/coding/1/')
        cant = Coding.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class IdentifierTypeTest(APITestCase):
    def test_createIdentifierType(self):
        """
        Asegura que el IdentifierType se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'coding': 'AAAA', 'text': 'IdentifierType'}
        cantIdentifierTypes = IdentifierType.objects.count()
        response = self.client.post('/common/identifier-type/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(IdentifierType.objects.count(),cantIdentifierTypes)

    def test_getIdentifierTypes(self):
        """
        Asegura obtener Codings
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createIdentifierType()
        response = self.client.get('/common/identifier-type/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierType(self):
        """
        Asegura obtener un Coding
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createIdentifierType()
        response = self.client.get('/common/identifier-type/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierTypeFiltered(self):
        """
        Asegura obtener un Coding con filtro
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createIdentifierType()
        response = self.client.get('/common/identifier-type/?coding=ARS',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deleteIdentifierType(self):
        """
        Asegura que se puedan eliminar Codings
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifierType()
        response = self.client.delete('/common/identifier-type/1/')
        cant = IdentifierType.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class IdentifierPeriodTest(APITestCase):
    def test_createIdentifierPeriod(self):
        """
        Asegura que el IdentifierPeriod se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        cantIdentifierPeriods = IdentifierPeriod.objects.count()
        response = self.client.post('/common/identifier-period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(IdentifierPeriod.objects.count(),cantIdentifierPeriods)

    def test_getIdentifierPeriods(self):
        """
        Asegura obtener IdentifierPeriod
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createIdentifierPeriod()
        response = self.client.get('/common/identifier-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierPeriod(self):
        """
        Asegura obtener un IdentifierPeriod
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createIdentifierPeriod()
        response = self.client.get('/common/identifier-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteIdentifierPeriod(self):
        """
        Asegura que se puedan eliminar IdentifierPeriod
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifierPeriod()
        response = self.client.delete('/common/identifier-period/1/')
        cant = IdentifierPeriod.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class ContactPointPeriodTest(APITestCase):
    def test_createContactPointPeriod(self):
        """
        Asegura que el ContactPointPeriod se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        cantContactPointPeriods = ContactPointPeriod.objects.count()
        response = self.client.post('/common/contact-point-period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(ContactPointPeriod.objects.count(),cantContactPointPeriods)

    def test_getContactPointPeriods(self):
        """
        Asegura obtener ContactPointPeriod
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createContactPointPeriod()
        response = self.client.get('/common/contact-point-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getContactPointPeriod(self):
        """
        Asegura obtener un ContactPointPeriod
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createContactPointPeriod()
        response = self.client.get('/common/contact-point-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteContactPointPeriod(self):
        """
        Asegura que se puedan eliminar ContactPointPeriod
        :return:
        """
        helper = CommonTestHelper()
        helper.createContactPointPeriod()
        response = self.client.delete('/common/contact-point-period/1/')
        cant = ContactPointPeriod.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class AddressPointPeriodTest(APITestCase):
    def test_createAddressPointPeriod(self):
        """
        Asegura que el AddressPointPeriod se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        cantAddressPointPeriods = AddressPointPeriod.objects.count()
        response = self.client.post('/common/address-point-period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(AddressPointPeriod.objects.count(),cantAddressPointPeriods)

    def test_getAddressPointPeriods(self):
        """
        Asegura obtener AddressPointPeriod
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createAddresPointPeriod()
        response = self.client.get('/common/address-point-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAddressPointPeriod(self):
        """
        Asegura obtener un AddressPointPeriod
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createAddresPointPeriod()
        response = self.client.get('/common/address-point-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteAddressPointPeriod(self):
        """
        Asegura que se puedan eliminar AddressPointPeriod
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddresPointPeriod()
        response = self.client.delete('/common/address-point-period/1/')
        cant = AddressPointPeriod.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class NamePeriodTest(APITestCase):
    def test_createNamePeriod(self):
        """
        Asegura que el NamePeriod se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        cantNamePeriods = NamePeriod.objects.count()
        response = self.client.post('/common/name-period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(NamePeriod.objects.count(),cantNamePeriods)

    def test_getNamePeriods(self):
        """
        Asegura obtener NamePeriod
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createNamePeriod()
        response = self.client.get('/common/name-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getNamePeriod(self):
        """
        Asegura obtener un NamePeriod
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createNamePeriod()
        response = self.client.get('/common/name-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteNamePeriod(self):
        """
        Asegura que se puedan eliminar NamePeriod
        :return:
        """
        helper = CommonTestHelper()
        helper.createNamePeriod()
        response = self.client.delete('/common/name-period/1/')
        cant = NamePeriod.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class HumanNameTest(APITestCase):
    def test_createHumanName(self):
        """
        Prueba la creación de un HumanName
        :return:
        """

        period = NamePeriod.objects.create(
            start = datetime.now(),
            end = datetime.now()
        )
        data = {'use':'usual', 'text':'Roberto Gomez', 'family':'Gomez', 'given':'Roberto','prefix':'Mr', 'suffix':'jr', 'period':'http://localhost:8000/common/name-period/1/'}
        response = self.client.post('/common/human-name/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getHumanNames(self):
        """
        Prueba obtener todos los HummanName
        :return:
        """
        helper = CommonTestHelper()
        helper.createHumanName()
        response = self.client.get('/common/human-name/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getHumanName(self):
        """
        Prueba ontener un HumanName
        :return:
        """
        helper = CommonTestHelper()
        helper.createHumanName()
        response = self.client.get('/common/human-name/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredHumanName(self):
        """
        Prueba obtener un HumanName con filtros
        :return:
        """
        helper = CommonTestHelper()
        helper.createHumanName()
        response = self.client.get('/common/human-name/?family=Gomez', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updateHumanName(self):
        """
        Prueba modificar un HumanName
        :return:
        """
        helper = CommonTestHelper()
        helper.createHumanName()
        data={'use':'official', 'text':'Roberto Juan', 'family':'Gomez', 'given':'Juan','prefix':'Mr', 'suffix':'jr', 'period':'http://localhost:8000/common/name-period/1/'}
        response = self.client.put('/common/human-name/1/', data, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.json()['given'],'Juan')

    def test_deleteHumanName(self):
        """
        Prueba eliminar un HumanName
        :return:
        """
        helper = CommonTestHelper()
        helper.createHumanName()
        response = self.client.delete('/common/human-name/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0,HumanName.objects.count())

class AddressLineTest(APITestCase):
    def test_createAddressLine(self):
        """
        Asegura que el NamePeriod se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'line':'Libertad 5899'}
        cantAddressLines = AddressLine.objects.count()
        response = self.client.post('/common/address-line/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(AddressLine.objects.count(),cantAddressLines)

    def test_getAddressLines(self):
        """
        Asegura obtener AddressLine
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createAddressLine()
        response = self.client.get('/common/address-line/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAddressLine(self):
        """
        Asegura obtener un AddressLine
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createAddressLine()
        response = self.client.get('/common/address-line/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteAddressLine(self):
        """
        Asegura que se puedan eliminar AddressLine
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddressLine()
        response = self.client.delete('/common/address-line/1/')
        cant = AddressLine.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class ContactPointTest(APITestCase):
    def test_createContactPoint(self):
        """
        Asegura que el ContactPoint se haya creado
        :return:
        """
        #url = reverse('coding-list')

        helper = CommonTestHelper()
        helper.createContactPointPeriod()

        data = {'system':'email', 'value':'sa@prueba.com', 'use':'home', 'rank':'1', 'period':'http://localhost:8000/common/contact-point-period/1/'}
        cantContactPoint = ContactPoint.objects.count()
        response = self.client.post('/common/contact-point/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(ContactPoint.objects.count(),cantContactPoint)

    def test_getContactPoints(self):
        """
        Asegura obtener ContactPoints
        :return:
        """
        #url = reverse('coding-list')
        helper = CommonTestHelper()
        helper.createContactPoint()
        response = self.client.get('/common/contact-point/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getContactPoint(self):
        """
        Asegura obtener un ContactPoint
        :return:
        """
        #url = reverse('coding-detail')
        helper = CommonTestHelper()
        helper.createContactPoint()
        response = self.client.get('/common/contact-point/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteContactPoint(self):
        """
        Asegura que se puedan eliminar ContactPoint
        :return:
        """
        helper = CommonTestHelper()
        helper.createContactPoint()
        response = self.client.delete('/common/contact-point/1/')
        cant = ContactPoint.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class AddressTest(APITestCase):

    def test_createAddress(self):
        """
        Asegura crear un Address
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddresPointPeriod()
        helper.createAddressLine()

        data= {'use': 'home','type': 'postal','text': 'Prueba','lines': ['http://localhost:8000/common/address-line/1/'],'city': 'Villa Libertad','district': 'San Martin','state': 'Buenos Aires','postalCode': '1650', 'country': 'Argentina','period': 'http://localhost:8000/common/address-point-period/1/'}
        cantAddress= Address.objects.count()
        response = self.client.post('/common/address/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(Address.objects.count(),cantAddress)

    def test_getAddresses(self):
        """
        Obtiene todas las Address
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddress()
        response = self.client.get('/common/address/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAddress(self):
        """
        Obtiene una address
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddress()
        response = self.client.get('/common/address/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredAddress(self):
        """
        Obtiene un address filtrado
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddress()
        response = self.client.get('/common/address/?use=home&type=postal&text=prueba',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteAddress(self):
        """
        Elinima un address
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddress()
        response = self.client.delete('/common/address/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Address.objects.count(),0)

    def test_updateAddress(self):
        """
        Modifica un Address
        :return:
        """
        helper = CommonTestHelper()
        helper.createAddress()
        data= {'use': 'home','type': 'postal','text': 'Prueba','lines': ['http://localhost:8000/common/address-line/1/'],'city': 'Villa Libertad','district': 'San Martin','state': 'Buenos Aires','postalCode': '1650', 'country': 'Brazil','period': 'http://localhost:8000/common/address-point-period/1/'}
        response = self.client.put('/common/address/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['country'],'Brazil')

class OrganizationContactTest(APITestCase):

    def test_createOrganizationContact(self):
        """
        Asegura crear un OrganizationContact
        :return:
        """
        helper = CommonTestHelper()
        helper.createHumanName()
        helper.createContactPoint()
        helper.createAddress()

        data= {'purpose': 'bill','name': 'http://localhost:8000/common/human-name/1/','telecom': 'http://localhost:8000/common/contact-point/1/','address': 'http://localhost:8000/common/address/1/'}
        cantContacts= OrganizationContact.objects.count()
        response = self.client.post('/common/organization-contact/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(Address.objects.count(),cantContacts)

    def test_getOrganizationContacts(self):
        """
        Obtiene todas las OrganizationContact
        :return:
        """
        helper = CommonTestHelper()
        helper.createOrganizationContact()
        response = self.client.get('/common/organization-contact/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getOrganizationContact(self):
        """
        Obtiene una OrganizationContact
        :return:
        """
        helper = CommonTestHelper()
        helper.createOrganizationContact()
        response = self.client.get('/common/organization-contact/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredOrganizationContact(self):
        """
        Obtiene un OrganizationContact filtrado
        :return:
        """
        helper = CommonTestHelper()
        helper.createOrganizationContact()
        response = self.client.get('/common/organization-contact/?purpose=bill',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteOrganizationContact(self):
        """
        Elinima un OrganizationContact
        :return:
        """
        helper = CommonTestHelper()
        helper.createOrganizationContact()
        response = self.client.delete('/common/organization-contact/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(OrganizationContact.objects.count(),0)

    def test_updateOrganizationContact(self):
        """
        Modifica un OrganizationContact
        :return:
        """
        helper = CommonTestHelper()
        helper.createOrganizationContact()
        helper.createHumanName()
        data= {'purpose': 'adm','name': 'http://localhost:8000/common/human-name/2/','telecom': 'http://localhost:8000/common/contact-point/1/','address': 'http://localhost:8000/common/address/1/'}
        response = self.client.put('/common/organization-contact/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['purpose'],'adm')
        self.assertEqual(response.json()['name'],'http://testserver/common/human-name/2/')

class IdentifierTest(APITestCase):


    def test_createIdentifier(self):
        """
        Asegura crear un Identifier(
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifierType()
        helper.createIdentifierPeriod()

        data= {'use': 'US','type': 'http://localhost:8000/common/identifier-type/1/','system': 'http://www.ingenia.la','value': '12345','period': 'http://localhost:8000/common/identifier-period/1/','assigner': 'Test'}
        response = self.client.post('/common/identifier/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getIdentifiers(self):
        """
        Obtiene todas las Identifier(
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifier()
        response = self.client.get('/common/identifier/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getOrganizationContact(self):
        """
        Obtiene una Identifier(
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifier()
        response = self.client.get('/common/identifier/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredIdentifier(self):
        """
        Obtiene un Identifier filtrado
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifier()
        response = self.client.get('/common/identifier/?use=US',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteIdentifier(self):
        """
        Elinima un Identifier
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifier()
        response = self.client.delete('/common/identifier/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Identifier.objects.count(),0)

    def test_updateIdentifier(self):
        """
        Modifica un Identifier
        :return:
        """
        helper = CommonTestHelper()
        helper.createIdentifier()
        helper.createIdentifierType()
        data= {'use': 'OF','type': 'http://localhost:8000/common/identifier-type/2/','system': 'http://www.ingenia.la','value': '12345','period': 'http://localhost:8000/common/identifier-period/1/','assigner': 'Test'}
        response = self.client.put('/common/identifier/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['use'],'OF')
        self.assertEqual(response.json()['type'],'http://testserver/common/identifier-type/2/')


class DayOfWeekTest(APITestCase):


    def test_createDayOfWeek(self):
        """
        Asegura crear un DayOfWeek
        :return:
        """
        data= {'value': 'mon'}
        response = self.client.post('/common/day-of-week/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getDaysOfWeek(self):
        """
        Obtiene todas las DayOfWeek(
        :return:
        """
        helper = CommonTestHelper()
        helper.createDayOfWeek()
        response = self.client.get('/common/day-of-week/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getDayOfWeek(self):
        """
        Obtiene una DayOfWeek(
        :return:
        """
        helper = CommonTestHelper()
        helper.createDayOfWeek()
        response = self.client.get('/common/day-of-week/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteDayOfWeek(self):
        """
        Elinima un DayOfWeek
        :return:
        """
        helper = CommonTestHelper()
        helper.createDayOfWeek()
        response = self.client.delete('/common/day-of-week/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Identifier.objects.count(),0)

class CommonTestHelper():
    def createDayOfWeek(self):
        """
        Crea un DayOfWeek
        :return:
        """
        day = DayOfWeek.objects.create(
            value = 'mon'
        )
        return day

    def createIdentifierType(self):
        """
        Crea un identifierType
        :return:
        """
        identifierType = IdentifierType.objects.create(
            coding="ARS",
            text="Pesos Argentinos"
        )
        return identifierType

    def createIdentifierPeriod(self):
        """
        Crea un IdentifierPeriod
        :return:
        """
        identifierPeriod = IdentifierPeriod.objects.create(
            start= datetime.now(),
            end=datetime.now()
        )
        return identifierPeriod

    def createIdentifier(self):
        """
        Crea un identifier
        :return:
        """
        identifierType = self.createIdentifierType()
        identifierPeriod = self.createIdentifierPeriod()
        identifier = Identifier.objects.create(
            use = "US",
            type = identifierType,
            system = "http://www.ingenia.la",
            value = "12345",
            period = identifierPeriod,
            assigner = "Test"
        )
        return identifier

    def createAddress(self):
        addressPointPeriod = self.createAddresPointPeriod()
        addressLine = self.createAddressLine()
        address = Address.objects.create(
            use = 'home',
            type= 'postal',
            text='prueba',
            city='villa Libertad',
            district='san Martin',
            state='Buenos Aires',
            postalCode='1650',
            country='Argentina'
        )
        address.period=addressPointPeriod
        address.lines.add(addressLine)
        address.save()
        return address

    def createContactPointPeriod(self):
        contactPointPeriod = ContactPointPeriod.objects.create(
            start= datetime.now(),
            end=datetime.now()
        )
        return contactPointPeriod

    def createContactPoint(self):
        contactPointPeriod = self.createContactPointPeriod()

        contactPoint = ContactPoint(
            system = "Email",
            value = "sa@prueba.com",
            use = "home",
            rank = 1,
            period = contactPointPeriod
        )
        contactPoint.save()

    def createOrganizationContact(self):
        address = self.createAddress()
        contactPoint = self.createContactPoint()
        name = self.createHumanName()

        return OrganizationContact.objects.create(
            purpose = 'bill',
            name = name,
            telecom = contactPoint,
            address = address
        )

    def createAddresPointPeriod(self):
        addressPointPeriod = AddressPointPeriod.objects.create(
            start= datetime.now(),
            end=datetime.now()
        )
        return addressPointPeriod

    def createAddressLine(self):
        addressLine = AddressLine.objects.create(
            line='Libertad 5899'
        )
        return addressLine

    def createHumanName(self):
        period = self.createNamePeriod()

        name = HumanName.objects.create(
            use = 'official',
            text = 'Roberto Gomez',
            family = 'Gomez',
            given = 'Roberto',
            prefix = 'Mr',
            suffix = None,
            period = period
        )

        return name

    def createNamePeriod(self):
        period = NamePeriod.objects.create(
            start = datetime.now(),
            end = datetime.now()
        )
        return period

    def createCoding(self):
        coding = Coding.objects.create(
            system = 'http://foo.test',
            version = '1.0',
            code = 'TES',
            display = 'TESTING',
            userSelected = False
        )
        return coding
