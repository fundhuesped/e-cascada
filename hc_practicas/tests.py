#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_practicas.models import Especialidad, Prestacion, Profesional, ProfesionalMeta
import datetime
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
            'especialidad': {'id':1}
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
            'especialidad': {'id':2}
        }
        response = self.client.put('/practicas/prestacion/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],'Consulta infectología 2')
        self.assertEqual(response.json()['description'],'Consulta infectología 2')
        self.assertEqual(response.json()['duration'],40)
        self.assertEqual(response.json()['notes'],'Consulta infectología 2')
        self.assertEqual(response.json()['default'],False)
        self.assertEqual(response.json()['especialidad']['id'],2)

class PacienteTest(APITestCase):
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

    def test_createPaciente(self):
        """
        Asegura crear un Paciente
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPrestacion()

        data= {
            'firstName': 'Cacho',
            'otherNames': 'Humberto Vicente',
            'fatherSurname': 'Castaña',
            'motherSurname': 'De los Limones',
            'birthDate': datetime.date(1942,6,11),
            'prestaciones':[{'id':1}]
        }
        response = self.client.post('/practicas/profesional/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profesional.objects.count(),1)

    def test_getPacientes(self):
        """
        Obtiene todos los Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.get('/practicas/profesional/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getProfesional(self):
        """
        Obtiene un Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.get('/practicas/profesional/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredProfesional(self):
        """
        Obtiene un Profesional filtrado por nombre y apellido
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.get('/practicas/profesional/?firstName=Cac&fatherSurename=Cas',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteProfesional(self):
        """
        Elinima un Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()
        response = self.client.delete('/practicas/profesional/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profesional.objects.count(),0)

    def test_updateProfesional(self):
        """
        Modifica un Profesional
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createProfesional()
        helperp.createPrestacion()
        data= {
            'firstName': 'Pepito',
            'otherNames': 'Jiminy',
            'fatherSurname': 'Grillo',
            'motherSurname': 'Cricket',
            'birthDate': datetime.date(1882,6,11),
            'prestaciones':[{'id':1},{'id':2}]
        }
        response = self.client.put('/practicas/profesional/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['firstName'],'Pepito')
        self.assertEqual(response.json()['otherNames'],'Jiminy')
        self.assertEqual(response.json()['fatherSurname'],'Grillo')
        self.assertEqual(response.json()['motherSurname'],'Cricket')

class ProfesionalMetaTest(APITestCase):
    def test_createProfesionalMeta(self):
        """
        Asegura crear un Meta Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesional()

        data= {
            'profesional': {'id':1},
            'metaType': 'PNS',
            'metaValue': 'Sucutrule'
        }
        response = self.client.post('/practicas/meta-profesional/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProfesionalMeta.objects.count(),1)

    def test_getProfesionalMetas(self):
        """
        Obtiene todos los Profesionales Metas
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesionalMeta()
        response = self.client.get('/practicas/meta-profesional/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getProfesionalMeta(self):
        """
        Obtiene un Meta Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesionalMeta()
        response = self.client.get('/practicas/meta-profesional/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredProfesionalMeta(self):
        """
        Obtiene un Meta Paciente filtrado por metaType
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesionalMeta()
        response = self.client.get('/practicas/meta-profesional/?metaType=PNS',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteProfesionalMeta(self):
        """
        Elinima un MEta Profesional
        :return:
        """
        helper = GatewayTestHelper()
        helper.createProfesionalMeta()
        response = self.client.delete('/practicas/meta-profesional/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ProfesionalMeta.objects.count(),0)

    def test_updateProfesionalMeta(self):
        """
        Modifica un Meta Profesional
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createProfesionalMeta()
        data= {
            'profesional': {'id':1},
            'metaType': 'PND',
            'metaValue': 'SARANDUNGA'
        }
        response = self.client.put('/practicas/meta-profesional/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['metaType'],'PND')
        self.assertEqual(response.json()['metaValue'],'SARANDUNGA')


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

    def createProfesional(self):
        prestacion = self.createPrestacion()
        profesional = Profesional.objects.create(
            firstName = 'Cacho',
            otherNames = 'Ruben Adolfo',
            fatherSurname = 'Castaña',
            motherSurname = 'De los Limones',
            birthDate = datetime.date(1942,6,11)
        )
        profesional.prestaciones.add(prestacion)
        profesional.save()

        return profesional

    def createProfesionalMeta(self):
        profesional = self.createProfesional()
        meta = ProfesionalMeta.objects.create(
            profesional = profesional,
            metaType = 'PNS',
            metaValue = 'Sucutrule'
        )

        return meta