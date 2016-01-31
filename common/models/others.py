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