from django.db.models import Q
from hc_practicas.models import Agenda
from hc_practicas.models import Ausencia
from hc_practicas.models import TurnoSlot
from hc_practicas.models import Turno
from hc_practicas.services import turno_service

def create_turno_slot(day, start, end, agenda, profesional, prestacion):
    """
    Valida el estado del turnoSlot a crear, lo crea y lo devuelve
    """


    #Falta validar si la prestacion, especialidad, agenda y profesional estan activos
    if get_active_ausencias_for_day_and_profesional(day, profesional):
        state = TurnoSlot.STATE_CONFLICT
    elif TurnoSlot.objects.filter((Q(end=end)
                                   |Q(start=start)
                                   |(Q(start__gt=start)
                                     &Q(end__lt=end))
                                   |(Q(start__lte=start)
                                     &Q(end__gt=start))
                                   |(Q(start__lt=end)
                                     &Q(end__gte=end))),
                                  day=day,
                                  state=TurnoSlot.STATE_OCCUPIED,
                                  profesional=profesional
                                 ).exists():
        state = TurnoSlot.STATE_CONFLICT
    else:
        state = TurnoSlot.STATE_AVAILABLE

    # Creo turnoSlot con los parametros y el estado
    turno_slot_instance = TurnoSlot.objects.create(
        day=day,
        start=start,
        end=end,
        state=state,
        agenda=agenda,
        profesional=profesional,
        prestacion=prestacion
    )
    turno_slot_instance.save()
    return turno_slot_instance

def activate_turno_slot(turno_slot):
    """
    Activa un cambiando el estdo de un turnoSlot deleted
    a libre o en conflicto
    """

    #Falta validar si la prestacion, especialidad, agenda y profesional estan activos
    if get_active_ausencias_for_day_and_profesional(turno_slot.day, turno_slot.profesional):
        turno_slot.state = TurnoSlot.STATE_CONFLICT
    elif TurnoSlot.objects.filter((Q(end=turno_slot.end)
                                   |Q(start=turno_slot.start)
                                   |(Q(start__gt=turno_slot.start)
                                     &Q(end__lt=turno_slot.end))
                                   |(Q(start__lte=turno_slot.start)
                                     &Q(end__gt=turno_slot.start))
                                   |(Q(start__lt=turno_slot.end)
                                     &Q(end__gte=turno_slot.end))),
                                  day=turno_slot.day,
                                  state=TurnoSlot.STATE_OCCUPIED,
                                  profesional=turno_slot.profesional
                                 ).exclude(pk=turno_slot.id).exists():
        turno_slot.state = TurnoSlot.STATE_CONFLICT
    else:
        turno_slot.state = TurnoSlot.STATE_AVAILABLE
    turno_slot.save()
    return

def release_turno_slot(turno_slot):
    """
    Libera un turno slot y saca de conflicto los asociados
    :return TurnoSlot
    """
    activate_conflicting_turno_slots(turno_slot)
    turno_slot.state = TurnoSlot.STATE_AVAILABLE
    turno_slot.save()
    return turno_slot

def activate_conflicting_turno_slots(turno_slot):
    """
    Chequea si las condiciones se dan para habilitar
    los turnoSlots que estaban en conflicto con el turno dado
    y los habilita.
    """

    if not get_active_ausencias_for_day_and_profesional(turno_slot.day,
                                                        turno_slot.profesional).exists():
        turno_slots = get_turno_slots_conflict_asociados(turno_slot.day,
                                                         turno_slot.start,
                                                         turno_slot.end,
                                                         turno_slot.profesional,
                                                         turno_slot.id)
        for turno_slot in turno_slots:
            turno_slot.state = TurnoSlot.STATE_AVAILABLE
            turno_slot.save()
    return

def conflict_asociated_turno_slots(original_turno_slot):
    """
    Chequea si las condiciones se dan para habilitar
    los turnos que estaban en conflicto con el turno dado
    y los habilita.
    """

    turno_slots = get_turno_slots_libres_asociados(original_turno_slot.day,
                                                   original_turno_slot.start,
                                                   original_turno_slot.end,
                                                   original_turno_slot.profesional,
                                                   original_turno_slot.id)
    for turno_slot in turno_slots:
        turno_slot.state = TurnoSlot.STATE_CONFLICT
        turno_slot.save()
    return

def get_turno_slots_conflict_asociados(day, start, end, profesional, original_turno_id):
    """
    Recupera los turnoSlots en conflicto con el dado.
    Controla que la agenda tambien este activa
    :return QuerySet
    """
    return  TurnoSlot.objects.filter((Q(end=end)
                                      |Q(start=start)
                                      |(Q(start__gt=start)
                                        &Q(end__lt=end))
                                      |(Q(start__lte=start)
                                        &Q(end__gt=start))
                                      |(Q(start__lt=end)
                                        &Q(end__gte=end))),
                                     day=day,
                                     status=TurnoSlot.STATUS_ACTIVE,
                                     profesional=profesional,
                                     agenda__status=Agenda.STATUS_ACTIVE,
                                     state=TurnoSlot.STATE_CONFLICT).exclude(pk=original_turno_id)
def occupy_turno_slot(turno_slot):
    """
    Cambia de estado al turnoSlot y pone en conlficto
    a los turnoSlot asociados
    :return TurnoSlot
    """
    conflict_asociated_turno_slots(turno_slot)
    turno_slot.state = TurnoSlot.STATE_OCCUPIED
    turno_slot.save()
    return turno_slot

def get_turno_slots_libres_asociados(day, start, end, profesional, original_turno_id):
    """
    Recupera los turnoSlots libres asociados con el dado
    Controla que la agenda tambien este activa
    :return QuerySet
    """
    return  TurnoSlot.objects.filter((Q(end=end)
                                      |Q(start=start)
                                      |(Q(start__gt=start)
                                        &Q(end__lt=end))
                                      |(Q(start__lte=start)
                                        &Q(end__gt=start))
                                      |(Q(start__lt=end)
                                        &Q(end__gte=end))),
                                     day=day,
                                     status=TurnoSlot.STATUS_ACTIVE,
                                     profesional=profesional,
                                     agenda__status=Agenda.STATUS_ACTIVE,
                                     state=TurnoSlot.STATE_AVAILABLE).exclude(pk=original_turno_id)


def conflict_turno_slot_unaware(turno_slot):
    """
    Pasa un turnoSlot a "conflicto" cancelando turnos
    si corresponde.
    No activa otros turnos
    """
    if turno_slot.state == TurnoSlot.STATE_OCCUPIED:
        turno_service.cancel_turno(turno_slot.currentTurno, Turno.CANCELATION_PROFESIONAL_ABSENT)
    turno_slot.state = TurnoSlot.STATE_CONFLICT
    turno_slot.save()

def delete_turno_slot(turno_slot):
    """
    Pasa un turnoSlot a "eliminado" activando los que colisionaban si corresponde
    """
    activate_conflicting_turno_slots(turno_slot)
    if turno_slot.state == TurnoSlot.STATE_OCCUPIED:
        turno_service.cancel_turno(turno_slot.currentTurno, Turno.CANCELATION_AGENDA_CHANGE)
    turno_slot.state = TurnoSlot.STATE_DELETED
    turno_slot.save()

def delete_turno_slot_unaware(turno_slot):
    """
    Pasa un turnoSlot a "eliminado"
    """
    turno_slot.state = TurnoSlot.STATE_DELETED
    turno_slot.status = TurnoSlot.STATUS_INACTIVE
    turno_slot.save()


# Esto debe ir en ausencias no en turnos
def get_active_ausencias_for_day_and_profesional(day, profesional):

    return Ausencia.objects.filter(start_day__lte=day,
                                   end_day__gte=day,
                                   profesional=profesional,
                                   status=Ausencia.STATUS_ACTIVE)
