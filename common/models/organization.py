from django.db import models

#Clase Organization
#Seg�n FHIR: "A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, etc."
#Mas informaci�n: https://www.hl7.org/fhir/organization.html
class Organization(models.Model):
    #Constantes para tipo de organizaci�n (https://www.hl7.org/fhir/valueset-organization-type.html)
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

    #Opciones de tipo de organizaci�n
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
