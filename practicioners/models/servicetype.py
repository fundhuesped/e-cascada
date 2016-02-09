from django.db import models
from .typeservice import TypeService
from .speciality import Speciality

#Clase ServiceType
#Specific service delivered or performed
class ServiceType(models.Model):
    type = models.ForeignKey(TypeService, null=False)
    speciality = models.ForeignKey(Speciality, null=False)