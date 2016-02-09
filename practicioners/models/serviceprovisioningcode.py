from django.db import models
from common.models import Coding

#Clase ServiceProvisioningCode
#Conditions under which service is available/offered (mas info: https://www.hl7.org/fhir/valueset-service-provision-conditions.html)
class ServiceProvisioningCode(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()