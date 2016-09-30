from django.db.models import Q
from hc_pacientes.models import Paciente
from hc_practicas.models import Turno

def cancel_turno(turno, reason=Turno.CANCELATION_OTHER):
    """
    Cancela un turno
    """
    turno.state = Turno.STATE_CANCELED
    turno.cancelation_reason = reason
    turno.save()
    return

def create_turno(turno_slot, paciente, notes=''):
    """
    Crea un turno
    :return Turno
    """
    turno = Turno.objects.create(turnoSlot=turno_slot,
                                 paciente=paciente,
                                 notes=notes,
                                 status=Turno.STATUS_ACTIVE,
                                 state=Turno.STATE_INITIAL)

    turno.save()
    return turno
