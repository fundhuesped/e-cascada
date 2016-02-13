from django.db import models
from .nameperiod import NamePeriod

#Clase HumanName
#Segn FHIR "A name of a human with text, parts and usage information."
#Mas Info: https://www.hl7.org/fhir/datatypes.html#HumanName
class HumanName(models.Model):
    #constantes para use (https://www.hl7.org/fhir/valueset-name-use.html)
    USUAL = 'usual'
    OFFICIAL = 'official'
    TEMP = 'temp'
    NICK = 'nickname'
    ANONYMOUS = 'anonymous'
    OLD = 'old'
    MAIDEN = 'maiden'

    #choices para use
    USE_CHOICES=(
        (USUAL, 'Usual'),
        (OFFICIAL, 'Official'),
        (TEMP, 'Temporal'),
        (NICK, 'Nickname'),
        (ANONYMOUS, 'Anonymous'),
        (OLD, 'Old'),
        (MAIDEN, 'Maiden')
    )

    use = models.CharField(max_length=9, choices=USE_CHOICES, default=USUAL)                #usual | official | temp | nickname | anonymous | old | maiden
    text = models.TextField()                                                               #Text representation of the full name
    family = models.TextField()                                                             #Family name (often called 'Surname') - debe devolverse como  una coleccin
    given = models.TextField()                                                              #Given names (not always 'first'). Includes middle names - debe devolverse como una coleccin
    prefix = models.TextField(null=True)                                                             #Parts that come before the name - debe devolverse como una coleccin
    suffix = models.TextField(null=True)                                                             #Parts that come after the name - debe devolverse como una coleccin
    period = models.OneToOneField(NamePeriod, null=True)                                    #Time period when name was/is in use
