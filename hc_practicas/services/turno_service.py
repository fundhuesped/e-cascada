from django.db.models import Q
from hc_practicas.models import Agenda
from hc_practicas.models import Ausencia
from hc_practicas.models import Turno

def create_turno(day, start, end, agenda, profesional, prestacion):
    """ Valida el estado del turno a crear, lo crea y lo devuelve """


    #Falta validar si la prestacion, especialidad, agenda y profesional estan activos
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
    else:
        status = Turno.STATUS_ACTIVE

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

def inactivate_taken_turno(turno):
    """
    Deshabilita un turno activando los que colisionaban si corresponde
    """
    turno.status = Turno.STATUS_INACTIVE
    turno.taken = False
    turno.paciente = None
    turno.save()

    activate_conflicting_turnos(turno)

def inactivate_taken_turno_unaware(turno):
    """
    Deshabilita un turno sin reactivar los turnos que colisionan
    """
    turno.status = Turno.STATUS_INACTIVE
    turno.taken = False
    turno.paciente = None
    turno.save()

def delete_turno(turno):
    """
    Elimina un turno activando los que colisionaban si corresponde
    """
    activate_conflicting_turnos(turno)
    turno.delete()

def activate_conflicting_turnos(turno):
    """
    Chequea si las condiciones se dan para habilitar
    los turnos que estaban en conflicto con el turno dado
    y los habilita.
    """

    if not get_active_ausencias_for_day_and_profesional(turno.day,
                                                        turno.profesional).exists():
        turnos = get_turnos_libres_desactivos_asociados(turno.day,
                                                        turno.start,
                                                        turno.end,
                                                        turno.profesional,
                                                        turno.id)
        for turno in turnos:
            activate_turno_unaware(turno)

def activate_turno(turno):
    """
    Chequea si corresponde activar el turno y lo activa
    """
    # Chequeo si hay ausencias
    if not get_active_ausencias_for_day_and_profesional(turno.day,
                                                        turno.profesional).exists():
        # Chequeo si no choca con otros turnos tomados
        if not get_turnos_tomados_asociados(turno.day,
                                            turno.start,
                                            turno.end,
                                            turno.profesional,
                                            turno.id).exists():
            turno.status = Turno.STATUS_ACTIVE
            turno.save()

def activate_turno_unaware(turno):
    """
    Activa un turno sin revisar dependencias
    """
    turno.status = Turno.STATUS_ACTIVE
    turno.save()

def get_turnos_tomados_asociados(day, start, end, profesional, original_turno_id):
    """
    Recupera los turnos asociados o en conflicto con el dado
    Controla que la agenda tambien este activa
    :return QuerySet
    """
    return  Turno.objects.filter((Q(end=end)
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
                                 agenda__status=Agenda.STATUS_ACTIVE,
                                 taken=True).exclude(pk=original_turno_id)

def get_turnos_libres_activos_asociados(day, start, end, profesional, original_turno_id):
    """
    Recupera los turnos libre y activos asociados o en conflicto con el dado
    Controla que la agenda tambien este activa
    :return QuerySet
    """
    return  Turno.objects.filter((Q(end=end)
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
                                 agenda__status=Agenda.STATUS_ACTIVE,
                                 taken=False).exclude(pk=original_turno_id)

def get_turnos_libres_desactivos_asociados(day, start, end, profesional, original_turno_id):
    """
    Recupera los turnos libre y desactivos asociados o en conflicto con el dado.
    Controla que la agenda tambien este activa
    :return QuerySet
    """
    return  Turno.objects.filter((Q(end=end)
                                  |Q(start=start)
                                  |(Q(start__gt=start)
                                    &Q(end__lt=end))
                                  |(Q(start__lte=start)
                                    &Q(end__gt=start))
                                  |(Q(start__lt=end)
                                    &Q(end__gte=end))),
                                 day=day,
                                 status=Turno.STATUS_INACTIVE,
                                 profesional=profesional,
                                 agenda__status=Agenda.STATUS_ACTIVE,
                                 taken=False).exclude(pk=original_turno_id)


# Esto debe ir en ausencias no en turnos
def get_active_ausencias_for_day_and_profesional(day, profesional):

    return Ausencia.objects.filter(start_day__lte=day,
                                   end_day__gte=day,
                                   profesional=profesional,
                                   status=Ausencia.STATUS_ACTIVE)
