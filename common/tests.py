import json
from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from common.models import Coding, IdentifierType, IdentifierPeriod, ContactPointPeriod, AddressPointPeriod, NamePeriod, AddressLine, ContactPoint

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
        response = self.client.get('/common/coding/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getCoding(self):
        """
        Asegura obtener un Coding
        :return:
        """
        #url = reverse('coding-detail')
        data = {'system': 'http://foo.test', 'version': '1.0', 'code': 'TES', 'display': 'TESTING','userSelected': 'false'}
        response = self.client.post('/common/coding/', data, format='json')
        response = self.client.get('/common/coding/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getCodingFiltered(self):
        """
        Asegura obtener un Coding con filtro
        :return:
        """
        #url = reverse('coding-list')
        data = {'system': 'http://foo.test', 'version': '1.0', 'code': 'TES', 'display': 'TESTING','userSelected': 'false'}
        response = self.client.post('/common/coding/', data, format='json')
        response = self.client.get('/common/coding/?code=TES&display=TESTING',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_deleteCoding(self):
        """
        Asegura que se puedan eliminar Codings
        :return:
        """
        data = {'system': 'http://foo.test', 'version': '1.0', 'code': 'TES', 'display': 'TESTING','userSelected': 'false'}
        response = self.client.post('/common/coding/', data, format='json')
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
        response = self.client.get('/common/identifier-type/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierType(self):
        """
        Asegura obtener un Coding
        :return:
        """
        #url = reverse('coding-detail')
        data = {'coding': 'AAAA', 'text': 'IdentifierType'}
        response = self.client.post('/common/identifier-type/', data, format='json')
        response = self.client.get('/common/identifier-type/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierTypeFiltered(self):
        """
        Asegura obtener un Coding con filtro
        :return:
        """
        #url = reverse('coding-list')
        data = {'coding': 'AAAA', 'text': 'IdentifierType'}
        response = self.client.post('/common/identifier-type/', data, format='json')
        response = self.client.get('/common/identifier-type/?coding=AAAA',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deleteIdentifierType(self):
        """
        Asegura que se puedan eliminar Codings
        :return:
        """
        data = {'coding': 'AAAA', 'text': 'IdentifierType'}
        response = self.client.post('/common/identifier-type/', data, format='json')
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
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/identifier-period/', data, format='json')
        response = self.client.get('/common/identifier-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierPeriod(self):
        """
        Asegura obtener un IdentifierPeriod
        :return:
        """
        #url = reverse('coding-detail')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/identifier-period/', data, format='json')
        response = self.client.get('/common/identifier-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierPeriodFiltered(self):
        """
        Asegura obtener un IdentifierPeriod con filtro
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/identifier-period/', data, format='json')
        response = self.client.get('/common/identifier-period/?start=2016-01-30 12:55&end=2016-01-31 13:00',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deleteIdentifierPeriod(self):
        """
        Asegura que se puedan eliminar IdentifierPeriod
        :return:
        """
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/identifier-period/', data, format='json')
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
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/contact-point-period/', data, format='json')
        response = self.client.get('/common/contact-point-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getContactPointPeriod(self):
        """
        Asegura obtener un ContactPointPeriod
        :return:
        """
        #url = reverse('coding-detail')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/contact-point-period/', data, format='json')
        response = self.client.get('/common/contact-point-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getContactPointPeriodFiltered(self):
        """
        Asegura obtener un ContactPointPeriod con filtro
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/contact-point-period/', data, format='json')
        response = self.client.get('/common/contact-point-period/?start=2016-01-30 12:55&end=2016-01-31 13:00',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deleteContactPointPeriod(self):
        """
        Asegura que se puedan eliminar ContactPointPeriod
        :return:
        """
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/contact-point-period/', data, format='json')
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

    def test_getIdentifierPeriods(self):
        """
        Asegura obtener AddressPointPeriod
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/address-point-period/', data, format='json')
        response = self.client.get('/common/address-point-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierPeriod(self):
        """
        Asegura obtener un AddressPointPeriod
        :return:
        """
        #url = reverse('coding-detail')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/address-point-period/', data, format='json')
        response = self.client.get('/common/address-point-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getIdentifierPeriodFiltered(self):
        """
        Asegura obtener un AddressPointPeriod con filtro
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/address-point-period/', data, format='json')
        response = self.client.get('/common/address-point-period/?start=2016-01-30 12:55&end=2016-01-31 13:00',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deleteIdentifierPeriod(self):
        """
        Asegura que se puedan eliminar AddressPointPeriod
        :return:
        """
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/address-point-period/', data, format='json')
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
        self.assertGreater(AddressPointPeriod.objects.count(),cantNamePeriods)

    def test_getNamePeriods(self):
        """
        Asegura obtener NamePeriod
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/name-period/', data, format='json')
        response = self.client.get('/common/name-period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getNamePeriod(self):
        """
        Asegura obtener un NamePeriod
        :return:
        """
        #url = reverse('coding-detail')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/name-period/', data, format='json')
        response = self.client.get('/common/name-period/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getNamePeriodFiltered(self):
        """
        Asegura obtener un NamePeriod con filtro
        :return:
        """
        #url = reverse('coding-list')
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/name-period/', data, format='json')
        response = self.client.get('/common/name-period/?start=2016-01-30 12:55&end=2016-01-31 13:00',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_deleteNamePeriod(self):
        """
        Asegura que se puedan eliminar NamePeriod
        :return:
        """
        data = {'start': '2016-01-30 12:55', 'end': '2016-01-31 13:00'}
        response = self.client.post('/common/name-period/', data, format='json')
        response = self.client.delete('/common/name-period/1/')
        cant = NamePeriod.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class AddressLineTest(APITestCase):
    def crearAddressLine(self):
        linea = AddressLine(line="Libertad 5899")
        linea.save()

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
        self.crearAddressLine()
        response = self.client.get('/common/address-line/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAddressLine(self):
        """
        Asegura obtener un AddressLine
        :return:
        """
        #url = reverse('coding-detail')
        self.crearAddressLine()
        response = self.client.get('/common/address-line/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteAddressLine(self):
        """
        Asegura que se puedan eliminar AddressLine
        :return:
        """
        self.crearAddressLine()
        response = self.client.delete('/common/address-line/1/')
        cant = AddressLine.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class ContactPointLineTest(APITestCase):
    def crearContactPoint(self):
        contactPointPeriod = ContactPointPeriod(
            start= datetime.now(),
            end=datetime.now()
        )
        contactPointPeriod.save()

        contactPoint = ContactPoint(
            system = "Email",
            value = "sa@prueba.com",
            use = "home",
            rank = 1,
            period = None
        )
        contactPoint.save()

    def test_createContactPoint(self):
        """
        Asegura que el ContactPoint se haya creado
        :return:
        """
        #url = reverse('coding-list')
        data = {'system':'Email', 'value':'sa@prueba.com', 'use':'home', 'rank':'1', 'period':None}
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
        self.crearContactPoint()
        response = self.client.get('/common/contact-point/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getContactPoint(self):
        """
        Asegura obtener un ContactPoint
        :return:
        """
        #url = reverse('coding-detail')
        self.crearContactPoint()
        response = self.client.get('/common/contact-point/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteContactPoint(self):
        """
        Asegura que se puedan eliminar ContactPoint
        :return:
        """
        self.crearContactPoint()
        response = self.client.delete('/common/contact-point/1/')
        cant = ContactPoint.objects.count()
        self.assertEqual(cant,0)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)