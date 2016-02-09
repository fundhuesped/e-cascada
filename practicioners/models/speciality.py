from django.db import models
from common.models import Coding

#Clase Speciality
#Specialties handled by the Service Site
class Speciality(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()