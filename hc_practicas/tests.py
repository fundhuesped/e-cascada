#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_practicas.models import Especialidad
from common.tests import CommonTestHelper
from rest_framework import status

class EspecialidadTest(APITestCase):
    def test_createEspecialidad(self):
        """
        Asegura crear una Especialidad
        :return:
        """
        data= {'name': 'Pediatría', 'description':'Especialidad dedicada a menores de 15 años'}
        response = self.client.post('/huesped/especialidad/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Especialidad.objects.count(),1)

    def test_getEspecialidades(self):
        """
        Obtiene todas las Especialidades
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/huesped/especialidad/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getEspecialidad(self):
        """
        Obtiene una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/huesped/especialidad/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredEspecialidad(self):
        """
        Obtiene una Especialidad filtrada
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/huesped/especialidad/?name=Ped',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteEspecialidad(self):
        """
        Elinima una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.delete('/huesped/especialidad/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Especialidad.objects.count(),0)

    def test_updateEspecialidad(self):
        """
        Modifica una Especialidad
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createEspecialidad()
        data= {'name': 'Pediatría pediatrica', 'description':'Especialidad dedicada a personas no mayores de 15 años'}
        response = self.client.put('/huesped/especialidad/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],'Pediatría pediatrica')
        self.assertEqual(response.json()['description'],'Especialidad dedicada a personas no mayores de 15 años')

class GatewayTestHelper():
    def createEspecialidad(self):
        especialidad = Especialidad.objects.create(
            name = 'Pediatria',
            description = 'Especialidad dedicada a menores de 15 años'
        )
        return especialidad