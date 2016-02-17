from django.db import models
from common.models import Identifier, ContactPoint, Address, Organization

class Location(models.Model):
    """
    Según HL7:
    A Location includes both incidental locations (a place which is used for healthcare without prior designation or authorization) and dedicated, formally appointed locations. Locations may be private, public, mobile or fixed and scale from small freezers to full hospital buildings or parking garages.

    Examples of Locations are:

    - Building, ward, corridor, room or bed
    - Mobile Clinic
    - Freezer, incubator
    - Vehicle or lift
    - Home, shed, or a garage
    - Road, parking place, a park
    - Ambulance (generic)
    - Ambulance (specific)
    - Patient's Home (generic)
    - Jurisdiction
    These locations are not intended to cover locations on a patient where something occurred (i.e. a patient's broken leg), but can hapily cover the location where the patient broke the leg (the playground)
    Más info: https://www.hl7.org/fhir/location.html
    """

    #Valores para status (https://www.hl7.org/fhir/valueset-location-status.html)
    STATUS_ACTIVE = 'active'
    STATUS_SUSPENDED = 'suspended'
    STATUS_INACTIVE = 'inactive'
    #Opciones para status
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_SUSPENDED, 'Suspended'),
        (STATUS_INACTIVE, 'Inactive')
    )

    #Valores para mode (https://www.hl7.org/fhir/valueset-location-mode.html)
    MODE_INSTANCE = 'instance'
    MODE_KIND = 'kind'
    #Opciones para mode
    MODE_CHOICES = (
        (MODE_INSTANCE, 'Instance'),
        (MODE_KIND, 'Kind')
    )

    #Valores para physicalType (https://www.hl7.org/fhir/valueset-location-physical-type.html)
    PT_BUILDING = 'bu'
    PT_WING = 'wi'
    PT_LEVEL = 'lvl'
    PT_CORRIDOR = 'co'
    PT_ROOM = 'ro'
    PT_BED = 'bd'
    PT_VEHICLE = 've'
    PT_HOUSE = 'ho'
    PT_CABINET = 'ca'
    PT_ROAD = 'rd'
    PT_JURISDICTION = 'jdn'
    PT_AREA = 'area'

    #Opciones para physicalType
    PT_CHOICES = (
        (PT_BUILDING, 'Building'),
        (PT_WING, 'Wing'),
        (PT_LEVEL, 'Level'),
        (PT_CORRIDOR, 'Corridor'),
        (PT_ROOM, 'Room'),
        (PT_BED, 'Bed'),
        (PT_VEHICLE, 'Vehicle'),
        (PT_HOUSE, 'House'),
        (PT_CABINET, 'Cabinet'),
        (PT_ROAD, 'Road'),
        (PT_JURISDICTION, 'Jurisdiction'),
        (PT_AREA, 'Area')
    )

    identifier = models.OneToOneField(Identifier)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    name = models.CharField(null=False, max_length=150)
    description = models.CharField(null=True,max_length=300)
    mode = models.CharField(max_length=8, choices=MODE_CHOICES, default=MODE_INSTANCE)
    type = models.CharField(null=True, max_length=6)
    telecom = models.ManyToManyField(ContactPoint)
    address = models.ManyToManyField(Address)
    physicalType = models.CharField(max_length=4, choices=PT_CHOICES, default=PT_BUILDING)
    positionLongitude = models.DecimalField(null = False, decimal_places=2, max_digits=3)
    positionLatitude = models.DecimalField(null = False, decimal_places=2, max_digits=3)
    positionAltitude = models.DecimalField(null = True, decimal_places=2, max_digits=3)
    managingOrganization = models.ForeignKey(Organization)
    partOf = models.ForeignKey('self', null=True)