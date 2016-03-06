from practicioners.models import *
from common.models import *
from datetime import date, time

class GatewayBaseModel():
    ANIO_LIMITE_PERIODO = 2199
    URL_BASE =  'http://www.fundacionfernandez.org/'
    SYSTEMNAME = 'HUESPED HC'

    #persona de contacto
    NOMBRE_CONTACTO = 'Ana'
    APELLIDO_CONTACTO = 'Massacane'
    PREFIJO_CONTACTO = 'Mrs'

    def createLocation(self):
        """
        Crea una location con los datos básicos de Huesped
        :return:
        """
        if Location.objects.count()==0:
            id = self.createIdentifier(Identifier.OFFICIAL, self.URL_BASE + 'location/','Location ID', self.SYSTEMNAME, 'authomatic')
            org = self.createOrganization()
            tel = self.createContactPoint(date.today(),date(self.ANIO_LIMITE_PERIODO, 12,31),ContactPoint.PHONE,'011 4808-2600',ContactPoint.WORK,1)
            add = self.createAddress(date.today(), date(self.ANIO_LIMITE_PERIODO, 12, 31),Address.WORK, Address.POSTAL,'Cerviño 3356','CABA','Ciudad Autónoma de Buenos Aires','Buenos Aires','C1425AGP','Argentina')

            location = Location.objects.create(
                identifier = id,
                status = Location.STATUS_ACTIVE,
                name = 'Hospital Fernandez - Central',
                description = 'Sede central del Hospital Fernandez',
                mode = Location.MODE_INSTANCE,
                type = 'Central',
                physicalType = Location.PT_BUILDING,
                positionLongitude = -58.4069217,
                positionLatitude = -34.5814104,
                positionAltitude = 0,
                managingOrganization = org,
                partOf = None
            )
            location.telecom.add(tel)
            location.address.add(add)
        else:
            location = Location.objects[0]
        return location

    def createDayOfWeek(self):
        """
        Crea un DayOfWeek
        :return:
        """
        if DayOfWeek.objects.count()==0:
            day = DayOfWeek.objects.create(
                value = 'mon'
            )
        else:
            day = DayOfWeek.objects.first()
        return day

    def createIdentifierType(self, coding, text):
        """
        Crea un IdentifierType
        :param coding: Coding
        :param text: Texto
        :return:
        """

        if IdentifierType.objects.filter(coding=coding, text=text).count()==0:
            identifierType = IdentifierType.objects.create(
                coding=coding,
                text=text
            )
        else:
            identifierType = IdentifierType.objects.filter(coding=coding, text=text)[0]

        return identifierType

    def createIdentifier(self, use, coding, text, system, assigner):
        """
        Crea un identifier para Huesped
        :return:
        """
        identifierType = self.createIdentifierType(coding, text)
        identifierPeriod = IdentifierPeriod.objects.create(start=date.today(), end=date(self.ANIO_LIMITE_PERIODO,12,31))
        identifier = Identifier.objects.create(
            use = use,
            type = identifierType,
            system = system,
            value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)),
            period = identifierPeriod,
            assigner = assigner
        )
        return identifier

    def createAddress(self, start, end, use, type, text, city, district, state, postalCode, country):
        """
        Crea la dirección para Huesped
        :param start: fecha de inicio de vigencia
        :param end: fecha de fin de vigencia
        :param use: Uso de la dirección
        :param type: Typo de dirección
        :param text: Texto
        :param city: Ciudad
        :param district: Districto
        :param state: Estado
        :param postalCode: Código postal
        :param country: Pais
        :return: Instancia de Address
        """

        if(Address.objects.filter(type=type, text=text, city=city, district=district, state=state, postalCode=postalCode, country=country).count()==0):
            addressPointPeriod = AddressPointPeriod.objects.create(
                start = start,
                end = end
            )

            address = Address.objects.create(
                period = addressPointPeriod,
                use = use,
                type= type,
                text=text,
                city=city,
                district=district,
                state=state,
                postalCode=postalCode,
                country=country
            )

            address.save()
        else:
            address=Address.objects.filter(type=type, text=text, city=city, district=district, state=state, postalCode=postalCode, country=country)[0]
        return address

    def createContactPoint(self, start, end, system, value, use, rank):


        if ContactPoint.objects.filter(system=system, value=value, use=use, rank=rank).count()==0:
            contactPointPeriod = ContactPointPeriod.objects.create(
                start=start,
                end=end
            )

            contactPoint = ContactPoint(
                system = system,
                value = value,
                use = use,
                rank = rank,
                period = contactPointPeriod
            )
            contactPoint.save()
        else:
            contactPoint = ContactPoint.objects.filter(system=system, value=value, use=use, rank=rank)[0]

        return contactPoint

    def createOrganizationContact(self):
        address = self.createAddress(date.today(), date(self.ANIO_LIMITE_PERIODO, 12, 31),Address.WORK, Address.POSTAL,'Cerviño 3356','CABA','Ciudad Autónoma de Buenos Aires','Buenos Aires','C1425AGP','Argentina')
        contactPoint = self.createContactPoint(date.today(),date(self.ANIO_LIMITE_PERIODO, 12,31),ContactPoint.PHONE,'011 4808-2600',ContactPoint.WORK,1)
        name = HumanName.objects.create(
            use = HumanName.OFFICIAL,
            text = self.NOMBRE_CONTACTO + ' ' + self.APELLIDO_CONTACTO,
            family = self.APELLIDO_CONTACTO,
            given = self.NOMBRE_CONTACTO,
            prefix = self.PREFIJO_CONTACTO,
            suffix = None,
            period = NamePeriod.objects.create(start=date.today(), end=date(self.ANIO_LIMITE_PERIODO,12,31))
        )

        contact= OrganizationContact.objects.create(
            purpose = OrganizationContact.ADMIN,
            name = name,
            telecom = contactPoint,
            address = address
        )
        return contact

    def createOrganization(self):
        identifier = self.createIdentifier(Identifier.OFFICIAL, self.URL_BASE + 'location/','Location ID', self.SYSTEMNAME, 'authomatic')
        active = True
        type = Organization.PROVIDER
        name = 'Hospital Fernandez'
        telecom = self.createContactPoint(date.today(),date(self.ANIO_LIMITE_PERIODO, 12,31),ContactPoint.PHONE,'011 4808-2600',ContactPoint.WORK,1)
        address = self.createAddress(date.today(), date(self.ANIO_LIMITE_PERIODO, 12, 31),Address.WORK, Address.POSTAL,'Cerviño 3356','CABA','Ciudad Autónoma de Buenos Aires','Buenos Aires','C1425AGP','Argentina')
        partOf = None
        contact = self.createOrganizationContact()
        org = Organization(
            identifier = identifier,
            active = active,
            type = type,
            name = name,
            partOf = partOf
        )
        org.save()
        org.telecom.add(telecom)
        org.address.add(address)
        org.contact.add(contact)
        return org

    def createCoding(self, version, code, display, userSelected):
        """
        Crea un Coding para Huesped
        :param version: Versión del código
        :param code: Código
        :param display: Texto a mostrar
        :param userSelected: Booleano indicando si es elegible por el usuario
        :return:
        """
        coding = Coding.objects.create(
            system = self.URL_BASE + '/coding/',
            version = version,
            code = code,
            display = display,
            userSelected = userSelected
        )
        return coding

    def createPersonLink(self):
        personlink = PersonLink.objects.create(
            target='http://localhost:8000/common/person/1/',
            assurance = PersonLink.LEVEL2
        )
        return personlink
    """
    def createPerson(self):
        helper = CommonTestHelper()

        person = Person.objects.create(
            identifier = helper.createIdentifier(),
            name = helper.createHumanName(),
            gender = Person.MALE,
            birthDate = datetime.now(),
            photo = 'http://www.facebook.com',
            managingOrganization = helper.createOrganization(),
            active = True
        )
        person.telecom.add(helper.createContactPoint())
        person.address.add(helper.createAddress())
        person.link.add(helper.createPersonLink())
        return person
    """

    def createAvailableTime(self):
        dayOfWeek = self.createDayOfWeek()

        atime = AvailableTime.objects.create(
            allDay = False,
            availableStartTime = time(0,0,0),
            availableEndTime = time(23,59,59),
        )

        atime.daysOfWeek.add(dayOfWeek)
        atime.save()

        return atime

    def createCharacteristic(self, text):
        coding = self.createCoding('1.0','ELE01','Elegibility',True)
        characteristic = Characteristic.objects.create(
            coding = coding,
            text = text
        )
        return characteristic

    def createEligibility(self, text):
        coding = self.createCoding('1.0','ELE01','Elegibility',True)
        eligibility = Eligibility.objects.create(
            coding = coding,
            text = text
        )
        return eligibility

    def createHealthCareService(self, serviceName, comment):


        if HealthcareService.objects.filter(serviceName=serviceName).count() == 0:
            identifier = self.createIdentifier(Identifier.OFFICIAL, self.URL_BASE + 'healthcareservice/','HealthCareService ID', self.SYSTEMNAME, 'authomatic')
            providedBy = self.createOrganization()
            serviceCategory = self.createServiceCategory('Servicio de salud')
            serviceType = self.createServiceType('Servicio de salud')
            location = 'Location a cambiar'
            serviceName = serviceName
            comment = comment
            extraDetails = None
            photo = None
            telecom = self.createContactPoint(date.today(),date(self.ANIO_LIMITE_PERIODO, 12,31),ContactPoint.PHONE,'011 4808-2600',ContactPoint.WORK,1)
            coverageArea = 'Location a cambiar'
            serviceProvisioningCode = self.createServiceProvisioningCode('SPC0001')
            eligibility = self.createEligibility('Servicio Elegible')
            eligibilityNote = None
            programName = None
            characteristic = self.createCharacteristic('Servicio consumible')
            referralMethod = self.createReferralMethod('Apto para referencias')
            publicKey = None
            appointmentRequired = True
            availableTime = self.createAvailableTime()
            notAvailable = None
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

            hcs.save()
        else:
            hcs = HealthcareService.objects.filter(serviceName=serviceName)[0]
        return hcs

    """
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
    """

    def createReferralMethod(self, text):
        coding = self.createCoding('1.0','RMED01','Referral Method',True)
        rmethod = ReferralMethod.objects.create(
            coding = coding,
            text = text
        )
        return rmethod

    """
    def createRole(self):
        commonHelper = CommonTestHelper()
        coding = commonHelper.createCoding()
        rol = Role.objects.create(
            coding = coding,
            text = "Role"
        )
        return rol
    """

    def createServiceCategory(self, text):
        coding = self.createCoding('1.0','SCAT01','Service Category',True)
        serviceCategory = ServiceCategory.objects.create(
            coding = coding,
            text = text
        )
        return serviceCategory

    def createServiceProvisioningCode(self, text):
        coding = self.createCoding('1.0','SPC01','Service Provisioning Code',True)
        sprovcode = ServiceProvisioningCode.objects.create(
            coding = coding,
            text = text
        )
        return sprovcode

    def createServiceType(self, text):
        type = self.createTypeService(text)
        spec = self.createSpeciality(text)
        stype = ServiceType.objects.create(
            type = type,
            speciality = spec
        )
        return stype

    def createSpeciality(self, text):
        coding = self.createCoding('1.0','SPEC01','Especialidad', True)
        spec = Speciality.objects.create(
            coding = coding,
            text = text
        )
        return spec

    def createTypeService(self, text):
        coding = self.createCoding('1.0','TSER01','Tipo de Servicio', True)
        tser = TypeService.objects.create(
            coding = coding,
            text = text
        )
        return tser