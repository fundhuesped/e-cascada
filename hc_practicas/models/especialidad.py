from django.db import models

class Especialidad(models.Model):
    """
    Clase que representa la información mínima necesaria para gestionar una Especialidad
    """
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo')
    )

    name = models.CharField(max_length=70, null=False)
    description = models.CharField(max_length=150, null=False)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=STATUS_ACTIVE)