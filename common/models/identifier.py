from django.db import models
__author__ = 'Santi'

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
