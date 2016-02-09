from django.db import models
from common.models import Coding

#Clase ReferralMethod
#Ways that the service accepts referrals (mas info: https://www.hl7.org/fhir/valueset-service-referral-method.html, https://www.hl7.org/fhir/terminologies.html#example)
class ReferralMethod(models.Model):
    coding = models.ForeignKey(Coding)
    text = models.TextField()