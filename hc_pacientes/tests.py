#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_common.tests import CommonTestHelper
from hc_pacientes.models import Paciente, PacienteMeta
from rest_framework import status
import datetime

class PacienteTest(APITestCase):
    def test_createPaciente(self):
        """
        Asegura crear un Paciente
        :return:
        """
        data= {
            'firstName': 'Cacho',
            'otherNames': 'Humberto Vicente',
            'fatherSurname': 'Castaña',
            'motherSurname': 'De los Limones',
            'birthDate': datetime.date(1942,6,11),
            'idpaciente':'AADDEE'
        }
        response = self.client.post('/pacientes/paciente/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Paciente.objects.count(),1)

    def test_getPacientes(self):
        """
        Obtiene todos los Pacientes
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.get('/pacientes/paciente/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPaciente(self):
        """
        Obtiene un Paciente
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.get('/pacientes/paciente/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredPaciente(self):
        """
        Obtiene un Paciente filtrado por nombre y apellido
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.get('/pacientes/paciente/?firstName=Cac&fatherSurename=Cas',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePaciente(self):
        """
        Elinima un Paciente
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()
        response = self.client.delete('/pacientes/paciente/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Paciente.objects.count(),0)

    def test_updatePaciente(self):
        """
        Modifica un Paciente
        :return:
        """
        helperp = PacienteTestHelper()
        helperp.createPaciente()
        data= {
            'firstName': 'Pepito',
            'otherNames': 'Jiminy',
            'fatherSurname': 'Grillo',
            'motherSurname': 'Cricket',
            'birthDate': datetime.date(1882,6,11),
            'idpaciente':'SARAZA'
        }
        response = self.client.put('/pacientes/paciente/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['firstName'],'Pepito')
        self.assertEqual(response.json()['otherNames'],'Jiminy')
        self.assertEqual(response.json()['fatherSurname'],'Grillo')
        self.assertEqual(response.json()['motherSurname'],'Cricket')

class PacienteMetaTest(APITestCase):
    def test_createPacienteMeta(self):
        """
        Asegura crear un Paciente
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPaciente()

        data= {
            'paciente': 'http://localhost/pacientes/paciente/1/',
            'metaType': 'PNS',
            'metaValue': 'Sucutrule'
        }
        response = self.client.post('/pacientes/meta-paciente/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PacienteMeta.objects.count(),1)

    def test_getPacienteMetas(self):
        """
        Obtiene todos los PacienteMetas
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPacienteMeta()
        response = self.client.get('/pacientes/meta-paciente/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPaciente(self):
        """
        Obtiene un Paciente
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPacienteMeta()
        response = self.client.get('/pacientes/meta-paciente/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredPaciente(self):
        """
        Obtiene un Paciente filtrado por nombre y apellido
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPacienteMeta()
        response = self.client.get('/pacientes/meta-paciente/?metaType=PNS',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePaciente(self):
        """
        Elinima un Paciente
        :return:
        """
        helper = PacienteTestHelper()
        helper.createPacienteMeta()
        response = self.client.delete('/pacientes/meta-paciente/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PacienteMeta.objects.count(),0)

    def test_updatePaciente(self):
        """
        Modifica un Paciente
        :return:
        """
        helperp = PacienteTestHelper()
        helperp.createPacienteMeta()
        data= {
             'paciente': 'http://localhost/pacientes/paciente/1/',
            'metaType': 'PND',
            'metaValue': 'SARANDUNGA'
        }
        response = self.client.put('/pacientes/meta-paciente/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['metaType'],'PND')
        self.assertEqual(response.json()['metaValue'],'SARANDUNGA')

class PacienteTestHelper():
    def createPaciente(self):
        paciente = Paciente.objects.create(
            firstName = 'Cacho',
            otherNames = 'Ruben Adolfo',
            fatherSurname = 'Castaña',
            motherSurname = 'De los Limones',
            birthDate = datetime.date(1942,6,11),
            idpaciente = 'AADDAEDD'
        )

        return paciente

    def createPacienteMeta(self):
        paciente = self.createPaciente()
        meta = PacienteMeta.objects.create(
            paciente = paciente,
            metaType = 'PNS',
            metaValue = 'Sucutrule'
        )

        return meta