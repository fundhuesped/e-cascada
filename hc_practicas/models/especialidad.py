from django.db import models

class Especialidad(models.Model):
    """
    Clase que representa la información mínima necesaria para gestionar HealthCareServices en Huesped
    """
    name = models.CharField(max_length=70, null=False)
    description = models.CharField(max_length=150, null=False)