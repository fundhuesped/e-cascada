from django.db import models

class PersonLink(models.Model):
    """
    Segun HL7: Link to a resource that concerns the same actual person.py
    """

    #Constantes para assurance
    LEVEL1 = 'level1'
    LEVEL2 = 'level2'
    LEVEL3 = 'level3'
    LEVEL4 = 'level4'

    #Opciones de level
    LEVEL_CHOICES = (
        (LEVEL1, 'Nivel 1'),
        (LEVEL2, 'Nivel 2'),
        (LEVEL3, 'Nivel 3'),
        (LEVEL4, 'Nivel 4')
    )

    target = models.URLField(null=False)                                                #URL a modelo de paciente, practicioner, persona
    assurance = models.CharField(max_length=6, choices=LEVEL_CHOICES, default=LEVEL1)   #https://www.hl7.org/fhir/valueset-identity-assuranceLevel.html