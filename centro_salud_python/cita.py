class Cita:
    """Una cita agendada entre un paciente y un profesional."""

    def __init__(self, id_cita, fecha, hora, paciente, profesional):
        self._id_cita = id_cita
        self._fecha = fecha
        self._hora = hora
        self._paciente = paciente
        self._profesional = profesional
        self._estado = "PENDIENTE"  # PENDIENTE, ATENDIDA, CANCELADA

    def confirmar_atendida(self):
        self._estado = "ATENDIDA"

    def cancelar(self):
        self._estado = "CANCELADA"

    def get_id_cita(self):
        return self._id_cita

    def get_fecha(self):
        return self._fecha

    def get_hora(self):
        return self._hora

    def get_estado(self):
        return self._estado

    def get_paciente(self):
        return self._paciente

    def get_profesional(self):
        return self._profesional

    def __str__(self):
        return (f"Cita {self._id_cita} - {self._paciente.get_nombres()} con "
                f"{self._profesional.get_nombres()} ({self._fecha} {self._hora}) "
                f"[{self._estado}]")
