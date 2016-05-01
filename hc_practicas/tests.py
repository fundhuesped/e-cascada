#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from hc_practicas.models import Especialidad, Prestacion, Profesional, Period, DayOfWeek, Agenda
from hc_common.tests import CommonTestHelper
import datetime, calendar
from rest_framework import status

class ProfesionalTest(APITestCase):
    def test_createProfesional(self):
        """
        Asegura crear un Profesional
        :return:
        """
        cth = CommonTestHelper()
        cth.createDocumentType()
        cth.createSexType()
        cth.createLocation()
        cth.createCivilStatus()
        cth.createEducationType()
        cth.createSocialService()
        helper = GatewayTestHelper()
        helper.createPrestacion()

        data= {
            "firstName": "Paciente",
            "otherNames": "Pacientito",
            "fatherSurname": "Prueba",
            "motherSurname": "Del test",
            "birthDate": datetime.date(year=1986,month=1,day=2),
            "email": "prueba@me.com",
            "street": "Calle",
            "postal": "1234",
            "status": "Active",
            "documentType": {
                "id": 1
            },
            "documentNumber": "25456111",
            "genderAtBirth": {
                "id": 1
            },
            "genderOfChoice": {
                "id": 1
            },
            "location": {
                "id": 1
            },
            "occupation": "Ocupacion",
            "civilStatus": {
                "id": 1
            },
            "education": {
                "id": 1
            },
            "socialService": {
                "id": 1
            },
            "socialServiceNumber": "AAADDD",
            "terms": True,
            "bornPlace": "Capital",
            "firstVisit": datetime.date(year=2015, month=3, day=5),
            "notes": "Notitas",
            "primaryPhoneNumber": "111444555",
            "primaryPhoneContact": "Yo",
            "primaryPhoneMessage": True,
            "secondPhoneNumber": "21454545",
            "secondPhoneContact": "El",
            "secondPhoneMessage": False,
            "thirdPhoneNumber": "45654654",
            "thirdPhoneContact": "Ella",
            "thirdPhoneMessage": False,
            "prestaciones":[
                {
                    "id":1
                }
            ]
        }
        response = self.client.post('/practicas/profesional/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profesional.objects.count(),1)

    def test_getProfesionales(self):
        """
        Obtiene todos los Profesionales
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
        helper = GatewayTestHelper()
        helper.createProfesional()
        cth = CommonTestHelper()
        cth.createDocumentType()
        cth.createSexType()
        cth.createLocation()
        cth.createCivilStatus()
        cth.createEducationType()
        cth.createSocialService()
        helper.createPrestacion()

        data= {
            "firstName": "Paciente 2",
            "otherNames": "Pacientito 2",
            "fatherSurname": "Prueba 2",
            "motherSurname": "Del test 2",
            "birthDate": datetime.date(year=1985,month=1,day=2),
            "email": "prueba@me.com.ar",
            "street": "Calle 2",
            "postal": "12342",
            "status": "Inactive",
            "documentType": {
                "id": 1
            },
            "documentNumber": "254561112",
            "genderAtBirth": {
                "id": 1
            },
            "genderOfChoice": {
                "id": 1
            },
            "location": {
                "id": 1
            },
            "occupation": "Ocupacion2",
            "civilStatus": {
                "id": 1
            },
            "education": {
                "id": 1
            },
            "socialService": {
                "id": 1
            },
            "socialServiceNumber": "AAADDDD",
            "terms": False,
            "bornPlace": "Capital2",
            "firstVisit": datetime.date(year=2014, month=3, day=5),
            "notes": "Notitas2",
            "primaryPhoneNumber": "1114445552",
            "primaryPhoneContact": "Yo2",
            "primaryPhoneMessage": False,
            "secondPhoneNumber": "214545452",
            "secondPhoneContact": "El2",
            "secondPhoneMessage": True,
            "thirdPhoneNumber": "456546542",
            "thirdPhoneContact": "Ella2",
            "thirdPhoneMessage": True,
            "prestaciones":[
                {
                    "id":1
                }
            ]
        }
        response = self.client.put('/practicas/profesional/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["firstName"], "Paciente 2")
        self.assertEqual(response.json()["otherNames"], "Pacientito 2")
        self.assertEqual(response.json()["fatherSurname"], "Prueba 2")
        self.assertEqual(response.json()["motherSurname"], "Del test 2")
        self.assertEqual(response.json()["birthDate"], "1985-01-02")
        self.assertEqual(response.json()["email"], "prueba@me.com.ar")
        self.assertEqual(response.json()["street"], "Calle 2")
        self.assertEqual(response.json()["postal"], "12342")
        self.assertEqual(response.json()["status"], "Inactive")
        self.assertEqual(response.json()["documentType"]["id"],1)
        self.assertEqual(response.json()["documentNumber"], "254561112")
        self.assertEqual(response.json()["genderAtBirth"]["id"],1)
        self.assertEqual(response.json()["genderOfChoice"]["id"],1)
        self.assertEqual(response.json()["location"]["id"],1)
        self.assertEqual(response.json()["occupation"],"Ocupacion2")
        self.assertEqual(response.json()["civilStatus"]["id"],1)
        self.assertEqual(response.json()["education"]["id"],1)
        self.assertEqual(response.json()["socialService"]["id"],1)
        self.assertEqual(response.json()["socialServiceNumber"],"AAADDDD")
        self.assertEqual(response.json()["bornPlace"],"Capital2")
        self.assertEqual(response.json()["notes"], "Notitas2")
        self.assertEqual(response.json()["primaryPhoneNumber"], "1114445552")
        self.assertEqual(response.json()["primaryPhoneContact"], "Yo2")
        self.assertEqual(response.json()["primaryPhoneMessage"], False)


class PeriodTest(APITestCase):
    def test_createPeriod(self):
        """
        Asegura crear un Periodo
        :return:
        """
        helper = GatewayTestHelper()
        helper.createDayOfWeek(),
        helper.createDayOfWeek()
        data= {
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
            'selected': False,
            'daysOfWeek': [
                {"id":1},
                {"id":2}
            ]
        }
        response = self.client.post('/practicas/period/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Period.objects.count(),1)

    def test_getPeriods(self):
        """
        Obtiene todos los Periodos
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPeriod()
        response = self.client.get('/practicas/period/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getPeriodo(self):
        """
        Obtiene un Periodo
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPeriod()
        response = self.client.get('/practicas/period/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletePeriod(self):
        """
        Elinima un Periodo
        :return:
        """
        helper = GatewayTestHelper()
        helper.createPeriod()
        response = self.client.delete('/practicas/period/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Period.objects.count(),0)

    def test_updatePeriod(self):
        """
        Modifica un Period
        :return:
        """
        helperp = GatewayTestHelper()
        helperp.createPeriod()
        helperp.createDayOfWeek()
        data= {
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
            'selected': False,
            'daysOfWeek': [
                {"id":1}
            ]
        }
        response = self.client.put('/practicas/period/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['start'], datetime.datetime.now().strftime('%H:%M:%S'))
        self.assertEqual(response.json()['end'],(datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'))
        self.assertEqual(response.json()['selected'], False)
        self.assertEqual(response.json()['daysOfWeek'][0]['id'], 1)


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


class AgendaTest(APITestCase):

    def test_createAgendaSinFecha(self):
        """
        Asegura crear una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()
        prof.prestaciones.add(pres)
        prof.save()
        helper.createDayOfWeek()
        helper.createDayOfWeek()

        data= {
            'status':'Active',
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'periods':[
                {
                    'start': datetime.datetime.now().strftime('%H:%M:%S'),
                    'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                    'selected': False,
                    'daysOfWeek': [
                        {"id":1},
                        {"id":2}
                    ]
                }
            ]
        }
        response = self.client.post('/practicas/agenda/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agenda.objects.count(),1)
        self.assertEqual(response.json()['validFrom'],datetime.date.today().strftime('%Y-%m-%d'))
        self.assertEqual(response.json()['validTo'],datetime.date(year=datetime.date.today().year,
                                                                 month=datetime.date.today().month,
                                                                 day=calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]).strftime('%Y-%m-%d'))

    def test_createAgenda(self):
        """
        Asegura crear una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()

        helper.createDayOfWeek()
        helper.createDayOfWeek()

        data= {
            'status':'Active',
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'validFrom':datetime.date.today().strftime('%Y-%m-%d'),
            'validTo' : (datetime.date.today()+datetime.timedelta(days=3)).strftime('%Y-%m-%d'),
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'periods':[
                {
                    'start': datetime.datetime.now().strftime('%H:%M:%S'),
                    'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                    'selected': False,
                    'daysOfWeek': [
                        {"id":1},
                        {"id":2}
                    ]
                }
            ]
        }
        response = self.client.post('/practicas/agenda/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agenda.objects.count(),1)

    def test_getAgendas(self):
        """
        Obtiene todas las Especialidades
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        response = self.client.get('/practicas/agenda/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAgenda(self):
        """
        Obtiene una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        response = self.client.get('/practicas/agenda/1/',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFilteredAgenda(self):
        """
        Obtiene una Agenda filtrada
        :return:
        """
        helper = GatewayTestHelper()
        helper.createEspecialidad()
        response = self.client.get('/practicas/agenda/?status=Active&profesional=1&prestacion=1',format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json())

    def test_deleteAgenda(self):
        """
        Elinima una Agenda
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        response = self.client.delete('/practicas/agenda/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agenda.objects.count(),0)

    def test_updateAgenda(self):
        """
        Modifica una Especialidad
        :return:
        """
        helper = GatewayTestHelper()
        helper.createAgenda()
        prof = helper.createProfesional()
        pres = helper.createPrestacion()
        prof.prestaciones.add(pres)
        prof.save()
        helper.createDayOfWeek()
        helper.createDayOfWeek()

        data= {
            'status':'Inactive',
            'start': datetime.datetime.now().strftime('%H:%M:%S'),
            'end': (datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'),
            'validFrom': datetime.date.today().strftime('%Y-%m-%d'),
            'validTo': (datetime.date.today()+datetime.timedelta(days=3)).strftime('%Y-%m-%d'),
            'profesional': {"id":1},
            'prestacion': {"id": 1},
            'periods':[
                {
                    'start': datetime.datetime.now().strftime('%H:%M:%S'),
                    'end': (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                    'selected': False,
                    'daysOfWeek': [
                        {"id":1},
                        {"id":2}
                    ]
                }
            ]
        }
        response = self.client.put('/practicas/agenda/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['status'],'Inactive')
        self.assertEqual(response.json()['start'],datetime.datetime.now().strftime('%H:%M:%S'))
        self.assertEqual(response.json()['end'],(datetime.datetime.now()+datetime.timedelta(hours=4)).strftime('%H:%M:%S'))
        self.assertEqual(response.json()['validFrom'],datetime.date.today().strftime('%Y-%m-%d'))
        self.assertEqual(response.json()['validTo'],(datetime.date.today()+datetime.timedelta(days=3)).strftime('%Y-%m-%d'))
        self.assertEqual(response.json()['profesional']['id'],1)
        self.assertEqual(response.json()['prestacion']['id'],1)

class GatewayTestHelper():
    def createAgenda(self):
        prof = self.createProfesional()
        pres = self.createPrestacion()
        agenda = Agenda.objects.create(
            status='Active',
            start = datetime.datetime.now(),
            end = datetime.datetime.now()+datetime.timedelta(hours=4),
            validFrom = datetime.date.today(),
            validTo = datetime.date.today()+datetime.timedelta(days=3),
            profesional = prof,
            prestacion = pres
        )
        return agenda

    def createProfesional(self):
        cth = CommonTestHelper()
        dt=cth.createDocumentType()
        st=cth.createSexType()
        loc= cth.createLocation()
        cs=cth.createCivilStatus()
        et=cth.createEducationType()
        ss=cth.createSocialService()

        profesional = Paciente.objects.create(
            firstName= "Paciente",
            otherNames= "Pacientito",
            fatherSurname= "Prueba",
            motherSurname= "Del test",
            birthDate= datetime.date(year=1986,month=1,day=2),
            email= "prueba@me.com",
            street= "Calle",
            postal= "1234",
            status= "Active",
            documentType = dt,
            documentNumber= "25456111",
            genderAtBirth=st,
            genderOfChoice=st,
            location=loc,
            occupation= "Ocupacion",
            civilStatus=cs,
            education=et,
            socialService=ss,
            socialServiceNumber= "AAADDD",
            terms= True,
            bornPlace= "Capital",
            firstVisit= datetime.date(year=2015, month=3, day=5),
            notes= "Notitas",
            primaryPhoneNumber= "111444555",
            primaryPhoneContact= "Yo",
            primaryPhoneMessage= True,
            secondPhoneNumber= "21454545",
            secondPhoneContact= "El",
            secondPhoneMessage= False,
            thirdPhoneNumber="45654654",
            thirdPhoneContact= "Ella",
            thirdPhoneMessage= False
        )

        return profesional

    def createPeriod(self):
        dow=self.createDayOfWeek()
        period = Period.objects.create(
            start = datetime.datetime.now(),
            end = datetime.datetime.now()+datetime.timedelta(minutes=30),
            selected = False
        )
        period.daysOfWeek.add(dow)
        return period

    def createDayOfWeek(self):
        dow = DayOfWeek.objects.create(
            index=1,
            name="Lunes",
            selected=False
        )
        return dow

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