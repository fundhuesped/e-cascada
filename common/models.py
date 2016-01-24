from django.db import models

#Clase Coding
#Según FHIR: "A Coding is a representation of a defined concept using a symbol from a defined "code system" - see Using Codes in resources for more details."
#Mas información: https://www.hl7.org/fhir/datatypes.html#Coding
class Coding(models.Model):
    system = models.URLField()                                  #Identity of the terminology system
    version = models.TextField()                                #Version of the system - if relevant
    code = models.TextField()                                   #Symbol in syntax defined by the system
    display = models.TextField()                                #Representation defined by the system
    userSelected = models.BooleanField()                        #If this coding was chosen directly by the user

#Clase IdentifierType
#Debe contener los valores descriptos en https://www.hl7.org/fhir/v2/0203/index.html
class IdentifierType(models.Model):
    coding = models.CharField(max_length=4)
    text = models.TextField()

    class Meta:
        ordering = ['text']

#Periodo de tiempo en el que el identificador es valido
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class IdentifierPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

# Clase Identifier.
# Segun FHIR: "A numeric or alphanumeric string that is associated with a single object or entity within a given system. Typically, identifiers are used to connect content in resources to external content available in other frameworks or protocols. Identifiers are associated with objects, and may be changed or retired due to human or system process and errors."
# Creado siguiendo estandar FHIR. Mas información en : https://www.hl7.org/fhir/datatypes.html#Identifier
class Identifier(models.Model):
    #constantes para definir el uso
    USUAL = 'US'
    OFFICIAL = 'OF'
    TEMPORAL = 'TE'
    SECONDARY = 'SE'

    #opciones de uso
    USE_CHOICES = (
        (USUAL, 'Usual use'),
        (OFFICIAL, 'Official use'),
        (TEMPORAL, 'Temporal use'),
        (SECONDARY, 'Secondary use')
    )


    use = models.CharField(max_length=2, choices=USE_CHOICES, default=OFFICIAL)
    type = models.ForeignKey("IdentifierType", null=True, on_delete=models.SET_NULL)                     #Description of identifier
    system = models.URLField()                                                              #The namespace for the identifier
    value = models.TextField(unique=True)                                                   #The value that is unique
    period = models.ForeignKey("IdentifierPeriod", null=True, on_delete=models.SET_NULL)
    assigner = models.ForeignKey("Organization", related_name="assign_for")

#Clase ContactPoint
#Según FHIR> Details for all kinds of technology-mediated contact points for a person or organization, including telephone, email, etc.
#Mas información: https://www.hl7.org/fhir/datatypes.html#ContactPoint
class ContactPoint(models.Model):
    #Constantes para system
    PHONE = 'phone'
    FAX = 'fax'
    EMAIL = 'email'
    PAGER = 'pager'
    FACEBOOK = 'fa' #custom value
    TWITTER = 'tw' #custom value
    OTHER = 'other'

    #Choices para system
    SYSTEM_CHOICES = (
        (PHONE, 'Phone'),
        (FAX, 'Fax'),
        (EMAIL, 'Email'),
        (PAGER, 'Pager'),
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (OTHER, 'Other')
    )

    #Constantes para use (https://www.hl7.org/fhir/valueset-contact-point-use.html)
    HOME = 'home'
    WORK = 'work'
    TEMP = 'temp'
    OLD = 'old'
    MOBILE = 'mob'

    #Choices para use
    USE_CHOICES = (
        (HOME, 'Home'),
        (WORK, 'Work'),
        (TEMP, 'Temp'),
        (OLD, 'Old'),
        (MOBILE, 'Mobile')
    )

    system = models.CharField(max_length=5, choices=SYSTEM_CHOICES, default=MOBILE)  #A system is required if a value is provided.
    value = models.TextField()                                                          #The actual contact point details
    use = models.CharField(max_length=4, choices=USE_CHOICES, default=HOME)             #home | work | temp | old | mobile - purpose of this contact point
    rank = models.PositiveIntegerField(default=1)                                       #Specify preferred order of use (1 = highest)
    period = models.ForeignKey("ContactPointPeriod")                                      #Time period when the contact point was/is in use

#Periodo de tiempo en el que el identificador es valido
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class ContactPointPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

#Clase Address
#Según FHIR: "A postal address. There are a variety of postal address formats defined around the world. Postal addresses are often also used to record a location that can be visited to find a patient or person."
#Más información: https://www.hl7.org/fhir/datatypes.html#Address
class Address(models.Model):
    #Constantes para use
    HOME = 'home'
    WORK = 'work'
    TEMP = 'temp'
    OLD = 'old'

    #Opciones de use
    USE_CHOICES = (
        (HOME, 'Home'),
        (WORK, 'Work'),
        (TEMP, 'Temp'),
        (OLD, 'Old')
    )

    #Constantes para type
    POSTAL = 'postal'
    PHYSICAL = 'physical'
    BOTH = 'both'

    #Opciones de Type
    TYPE_CHOICES = (
        (POSTAL, 'Postal Address'),
        (PHYSICAL, 'Physical Address'),
        (BOTH, 'Physical and Postal Address')
    )

    use = models.CharField(max_length=4, choices=USE_CHOICES, default=HOME)                     #Home | work | temp | old - purpose of this address
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default=BOTH)                   #postal | physical | both
    text = models.TextField()                                                                   #Text representation of the address
    line = models.ManyToManyField("AddressLine")                                                  #Street name, number, direction & P.O. Box etc.
    city = models.TextField()                                                                   #Name of city, town etc.
    district = models.TextField()                                                               #District name (aka county)
    state = models.TextField()                                                                  #Sub-unit of country (abbreviations ok)
    postalCode = models.TextField()                                                             #Postal code for area
    country = models.TextField()                                                                #Country (can be ISO 3166 3 letter code)
    period = models.ForeignKey("AddressPointPeriod")                                              #Time period when address was/is in use

#Periodo de tiempo en el que una dirección es valida
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class AddressPointPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()


#Class AddressLine
#Street name, number, direction & P.O. Box etc.
#Clase creada para compatibilidad con el estandar FHIR, para que una Addres contenga muchas AddressLines
class AddressLine(models.Model):
    line = models.TextField()


#Clase HumanName
#Según FHIR "A name of a human with text, parts and usage information."
#Mas Info: https://www.hl7.org/fhir/datatypes.html#HumanName
class HumanName(models.Model):
    #constantes para use (https://www.hl7.org/fhir/valueset-name-use.html)
    USUAL = 'usual'
    OFFICIAL = 'official'
    TEMP = 'temp'
    NICK = 'nickname'
    ANONYMOUS = 'anonymous'
    OLD = 'old'
    MAIDEN = 'maiden'

    #choices para use
    USE_CHOICES=(
        (USUAL, 'Usual'),
        (OFFICIAL, 'Official'),
        (TEMP, 'Temporal'),
        (NICK, 'Nickname'),
        (ANONYMOUS, 'Anonymous'),
        (OLD, 'Old'),
        (MAIDEN, 'Maiden')
    )

    use = models.CharField(max_length=9, choices=USE_CHOICES, default=USUAL)                #usual | official | temp | nickname | anonymous | old | maiden
    text = models.TextField()                                                               #Text representation of the full name
    family = models.TextField()                                                             #Family name (often called 'Surname') - debe devolverse como  una colección
    given = models.TextField()                                                              #Given names (not always 'first'). Includes middle names - debe devolverse como una colección
    prefix = models.TextField()                                                             #Parts that come before the name - debe devolverse como una colección
    suffix = models.TextField()                                                             #Parts that come after the name - debe devolverse como una colección
    period = models.ForeignKey("NamePeriod")                                                  #Time period when name was/is in use

#Periodo de tiempo en el que un nombre es valido
#La estructura sigue las definiciones de FHIR en https://www.hl7.org/fhir/datatypes.html#Period
class NamePeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

#Clase OrganizationContact
#Según FHIR= "Contact for the organization for a certain purpose"
class OrganizationContact(models.Model):
    #Constantes para type (https://www.hl7.org/fhir/valueset-contactentity-type.html)
    BILL = 'bill'
    ADMIN = 'adm'
    HR = 'hr'
    PAYOR = 'pay'
    PATINF = 'pat'
    PRESS = 'pres'

    #Opciones del purpose
    PURPOSE_CHOICES = (
        (BILL, 'Billing'),
        (ADMIN, 'Administrative'),
        (HR, 'Human Resource'),
        (PAYOR, 'Payor'),
        (PATINF, 'Patient'),
        (PRESS, 'Press')
    )

    purpose = models.CharField(max_length=4, choices=PURPOSE_CHOICES, default=ADMIN)                #The type of contact
    name = models.ForeignKey("HumanName")                                                             #A name associated with the contact
    telecom = models.ForeignKey("ContactPoint")                                                       #Contact details (telephone, email, etc.) for a contact
    address = models.ForeignKey("Address")                                                            #Visiting or postal addresses for the contact


#Clase Organization
#Según FHIR: "A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, etc."
#Mas información: https://www.hl7.org/fhir/organization.html
class Organization(models.Model):
    #Constantes para tipo de organización (https://www.hl7.org/fhir/valueset-organization-type.html)
    PROVIDER = 'PROV'
    DEPARTMENT = 'DEPT'
    ORG_TEAM = 'TEAM'
    GOVERNMENT = 'GOVT'
    INS_COMPANY = 'INS'
    EDU_INSTITUTE = 'EDU'
    REL_INSTITUTE = 'REL'
    CLI_RES_SPONSOR = 'CRS'
    COM_GROUP = 'CG'
    BUSS_OR_CORP = 'BUS'
    OTHER = 'OTHER'

    #Opciones de tipo de organización
    TYPE_CHOICES = (
        (PROVIDER, 'Healthcare Provider'),
        (DEPARTMENT, 'Hospital Department'),
        (ORG_TEAM, 'Organizational team'),
        (GOVERNMENT, 'Government'),
        (INS_COMPANY, 'Insurance Company'),
        (EDU_INSTITUTE, 'Educational Institute'),
        (REL_INSTITUTE,'Religious Institution'),
        (CLI_RES_SPONSOR, 'Clinical Research Sponsor'),
        (COM_GROUP,'Community Group'),
        (BUSS_OR_CORP,'Non-Healthcare Business or Corporation'),
        (OTHER,'Other')
    )

    identifier = models.ForeignKey("Identifier", on_delete=models.CASCADE)                           #Identifies this organization across multiple systems
    active = models.BooleanField()                                                          #Whether the organization's record is still in active use
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=DEPARTMENT)         #Kind of organization
    name = models.TextField()                                                               #Name used for the organization
    telecom = models.ManyToManyField("ContactPoint")                                          #A contact detail for the organization The telecom of an organization can never be of use 'home'
    address = models.ManyToManyField("Address")                                               #An address for the organization. An address of an organization can never be of use 'home'
    partOf = models.ForeignKey('self')                                                      #The organization of which this organization forms a part
    contact = models.ManyToManyField("OrganizationContact")                                   #Contact for the organization for a certain purpose


#Dias de la semana
class DayOfWeek(models.Model):
    #constantes de daysofWeek
    MON = 'mon'
    TUE = 'tue'
    WED = 'wed'
    THU = 'thu'
    FRI = 'fri'
    SAT = 'sat'
    SUN = 'sun'

    #Choices para daysOfWeek
    DOW_CHOICES = (
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday')
    )
    value = models.CharField(max_length=3, choices=DOW_CHOICES, default=MON)                 #Valor del día de la semana