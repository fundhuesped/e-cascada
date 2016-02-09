from django.db import models
from common.models import Coding

#Clase Eligibility
#Specific eligibility requirements required to use the service
class Eligibility(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()