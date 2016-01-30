from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from common.models import Coding, IdentifierType, IdentifierPeriod, ContactPointPeriod, AddressPointPeriod

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