#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_common.models import Documento, Persona
from rest_framework import status
import datetime

class DocumentoTest(APITestCase):
    def test_createDocumento(self):
        """
        Asegura crear un Documento
        :return:
        """
        helper = CommonTestHelper()
        helper.createPersona()

        data= {
            'type': Documento.TYPE_DNI,
            'number': 28508869,
            'comments': 'Prueba',
            'persona':'http://localhost:80/comun/persona/1/'
        }
        response = self.client.post('/comun/documento/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Documento.objects.count(),1)

    def test_getDocumentos(self):
        """
        Obtiene todos los Documentos
        :return:
        """
        helper = CommonTestHelper()
        helper.createDocumento()
        response = self.client.get('/comun/documento/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getDocumento(self):
        """
        Obtiene un Documento
        :return:
        """
        helper = CommonTestHelper()
        helper.createDocumento()
        response = self.client.get('/comun/documento/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteDocumento(self):
        """
        Elinima un Documento
        :return:
        """
        helper = CommonTestHelper()
        helper.createDocumento()
        response = self.client.delete('/comun/documento/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Documento.objects.count(),0)

    def test_updateDocumento(self):
        """
        Modifica una Especialidad
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createDocumento()
        helperp.createPersona()

        data= {
            'type': Documento.TYPE_PASSPORT,
            'number': 30916044,
            'comments': 'Prueba 2',
            'persona':'http://localhost:80/comun/persona/2/'
        }
        response = self.client.put('/comun/documento/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['type'],Documento.TYPE_PASSPORT)
        self.assertEqual(response.json()['number'],30916044)
        self.assertEqual(response.json()['comments'],'Prueba 2')
        self.assertEqual(response.json()['persona'],'http://testserver/comun/persona/2/')


class PersonaTest(APITestCase):
    def test_createPersona(self):
        """
        Asegura crear una Persona
        :return:
        """
        data= {
            'firstName': 'Cacho',
            'otherNames': 'Humberto Vicente',
            'fatherSurname': 'Castaña',
            'motherSurname': 'De los Limones',
            'birthDate': datetime.date(1942,6,11)
        }
        response = self.client.post('/comun/persona/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Persona.objects.count(),1)

    def test_getPersonas(self):
        """
        Obtiene todas las Personas
        :return:
        """
        helper = CommonTestHelper()
        helper.createPersona()
        response = self.client.get('/comun/persona/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPersona(self):
        """
        Obtiene una Persona
        :return:
        """
        helper = CommonTestHelper()
        helper.createPersona()
        response = self.client.get('/comun/persona/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredPersona(self):
        """
        Obtiene una Persona filtrada por nombre y apellido
        :return:
        """
        helper = CommonTestHelper()
        helper.createPersona()
        response = self.client.get('/comun/persona/?firstName=Cac&fatherSurename=Cas',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePersona(self):
        """
        Elinima una Persona
        :return:
        """
        helper = CommonTestHelper()
        helper.createPersona()
        response = self.client.delete('/comun/persona/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Persona.objects.count(),0)

    def test_updatePersona(self):
        """
        Modifica una Persona
        :return:
        """
        helperp = CommonTestHelper()
        helperp.createPersona()
        data= {
            'firstName': 'Pepito',
            'otherNames': 'Jiminy',
            'fatherSurname': 'Grillo',
            'motherSurname': 'Cricket',
            'birthDate': datetime.date(1882,6,11)
        }
        response = self.client.put('/comun/persona/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['firstName'],'Pepito')
        self.assertEqual(response.json()['otherNames'],'Jiminy')
        self.assertEqual(response.json()['fatherSurname'],'Grillo')
        self.assertEqual(response.json()['motherSurname'],'Cricket')


class CommonTestHelper():
    def createDocumento(self):
        pers = self.createPersona()
        documento = Documento.objects.create(
            type = Documento.TYPE_DNI,
            number=28508869,
            comments='Prueba',
            persona = pers
        )
        return documento

    def createPersona(self):
        persona = Persona.objects.create(
            firstName = 'Cacho',
            otherNames = 'Ruben Adolfo',
            fatherSurname = 'Castaña',
            motherSurname = 'De los Limones',
            birthDate = datetime.date(1942,6,11)
        )

        return persona

