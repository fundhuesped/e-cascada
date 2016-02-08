from django.db import models
from common.models import Coding

#Clase ServiceCategory
#Son las diferentes categor�as a las que puede pertenecer un servicio
class ServiceCategory(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()