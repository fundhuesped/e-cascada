from django.db import models
import string, random

__author__ = 'Santi'

# Clase Identifier.
# Segun FHIR: "A numeric or alphanumeric string that is associated with a single object or entity within a given system. Typically, identifiers are used to connect content in resources to external content available in other frameworks or protocols. Identifiers are associated with objects, and may be changed or retired due to human or system process and errors."
# Creado siguiendo estandar FHIR. Mas informaci�n en : https://www.hl7.org/fhir/datatypes.html#Identifier
class Identifier(models.Model):
    def __init__(self, *args, **kvargs):
        self.value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Identifier, self).__init__(*args, **kvargs)

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
    value = models.TextField(unique=True, max_length=6)                                                   #The value that is unique
    period = models.OneToOneField("IdentifierPeriod", null=True, on_delete=models.SET_NULL) #Periodo de validez del Identifier
    assigner = models.TextField(null=True)                                                  #Organización que generó el ID (según HL7 puede ser solo texto para evitar dependencia cruzada)
