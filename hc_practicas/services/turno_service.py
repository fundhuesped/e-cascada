from django.db.models import Q
from hc_practicas.models import Ausencia
from hc_practicas.models import Turno

def create(day, start, end, agenda, profesional, prestacion):
    """ Valida el estado del turno a crear, lo crea y lo devuelve """
    if get_active_ausencias_for_day_and_profesional(day, profesional):
        status = Turno.STATUS_INACTIVE
    elif Turno.objects.filter((Q(end=end)
                               |Q(start=start)
                               |(Q(start__gt=start)
                                 &Q(end__lt=end))
                               |(Q(start__lte=start)
                                 &Q(end__gt=start))
                               |(Q(start__lt=end)
                                 &Q(end__gte=end))),
                              day=day,
                              status=Turno.STATUS_ACTIVE,
                              profesional=profesional,
                              taken=True).exists():
        status = Turno.STATUS_INACTIVE

    # Creo turno con los parametros y el estado
    turno_instance = Turno.objects.create(
        day=day,
        start=start,
        end=end,
        status=status,
        agenda=agenda,
        profesional=profesional,
        prestacion=prestacion
    )
    turno_instance.save()
    return turno_instance

def get_active_ausencias_for_day_and_profesional(day, profesional):

    return Ausencia.objects.filter(start_day__lte=day,
                                   end_day__gte=day,
                                   profesional=profesional,
                                   status=Ausencia.STATUS_ACTIVE)
