#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_practicas.models import Especialidad, Prestacion
from rest_framework import status

class EspecialidadTest(APITestCase):
    def test_createEspecialidad(self):
        """
        Asegura crear una Especialidad
        :return:
        """
        data= {'name': 'Pediatría', 'description':'Especialidad dedicada a menores de 15 años', 'status':'Active'}
        response = self.client.post('/practicas/especialidad/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Especialidad.objects.count(),1)

    def test_getEspecialidades(self):
        """
        Obtiene todas las Especialidades
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/especialidad/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getEspecialidad(self):
        """
        Obtiene una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/especialidad/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredEspecialidad(self):
        """
        Obtiene una Especialidad filtrada
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/especialidad/?name=Ped',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteEspecialidad(self):
        """
        Elinima una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.delete('/practicas/especialidad/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Especialidad.objects.count(),0)

    def test_updateEspecialidad(self):
        """
        Modifica una Especialidad
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createEspecialidad()
        data= {'name': 'Pediatría pediatrica', 'description':'Especialidad dedicada a personas no mayores de 15 años', 'status':'Active'}
        response = self.client.put('/practicas/especialidad/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],'Pediatría pediatrica')
        self.assertEqual(response.json()['description'],'Especialidad dedicada a personas no mayores de 15 años')

class PrestacionTest(APITestCase):
    def test_createPrestacion(self):
        """
        Asegura crear una Prestacion
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()

        data = {
            'name': 'Consulta infectología 2',
            'description': 'Consulta infectología 2',
            'duration': 40,
            'status': Prestacion.STATUS_INACTIVE,
            'notes': 'Consulta infectología 2',
            'default': False,
            'especialidad': 'http://localhost:8000/practicas/especialidad/1/'
        }

        response = self.client.post('/practicas/prestacion/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Prestacion.objects.count(),1)

    def test_getPrestacioneses(self):
        """
        Obtiene todas las Prestaciones
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.get('/practicas/prestacion/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPrestacion(self):
        """
        Obtiene una Prestacion
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.get('/practicas/prestacion/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredPrestacion(self):
        """
        Obtiene una Prestacion filtrada
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.get('/practicas/prestacion/?name=Ped&status=Active',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deletePrestacion(self):
        """
        Elinima una Prestacion
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()
        response = self.client.delete('/practicas/prestacion/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Prestacion.objects.count(),0)

    def test_updatePrestacion(self):
        """
        Modifica una Prestacion
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createPrestacion()
        helperp.createEspecialidad()

        data = {
            'name': 'Consulta infectología 2',
            'description': 'Consulta infectología 2',
            'duration': 40,
            'status': Prestacion.STATUS_INACTIVE,
            'notes': 'Consulta infectología 2',
            'default': False,
            'especialidad': 'http://localhost:8000/practicas/especialidad/2/'
        }
        response = self.client.put('/practicas/prestacion/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],'Consulta infectología 2')
        self.assertEqual(response.json()['description'],'Consulta infectología 2')
        self.assertEqual(response.json()['duration'],40)
        self.assertEqual(response.json()['notes'],'Consulta infectología 2')
        self.assertEqual(response.json()['default'],False)
        self.assertEqual(response.json()['especialidad'],'http://testserver/practicas/especialidad/2/')

class GatewayTestHelper():
    def createEspecialidad(self):
        especialidad = Especialidad.objects.create(
            name = 'Pediatria',
            description = 'Especialidad dedicada a menores de 15 años',
            status = Especialidad.STATUS_ACTIVE,
        )
        return especialidad

    def createPrestacion(self):
        especialidad = self.createEspecialidad()
        prestacion = Prestacion.objects.create(
            name = 'Consulta infectología',
            description = 'Consulta infectología',
            duration = 20,
            status = Prestacion.STATUS_ACTIVE,
            default=False,
            notes = 'Consulta infectología',
            especialidad = especialidad
        )
        return prestacion
