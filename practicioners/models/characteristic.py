from django.db import models
from common.models import Coding

#Clase Characteristic
#Characteristics (attributes)
class Characteristic(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()