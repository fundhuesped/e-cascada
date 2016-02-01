from django.db import models

#Clase Coding
#Seg�n FHIR: "A Coding is a representation of a defined concept using a symbol from a defined "code system" - see Using Codes in resources for more details."
#Mas informaci�n: https://www.hl7.org/fhir/datatypes.html#Coding
class Coding(models.Model):
    system = models.URLField()                                  #Identity of the terminology system
    version = models.TextField()                                #Version of the system - if relevant
    code = models.TextField()                                   #Symbol in syntax defined by the system
    display = models.TextField()                                #Representation defined by the system
    userSelected = models.BooleanField()                        #If this coding was chosen directly by the user
