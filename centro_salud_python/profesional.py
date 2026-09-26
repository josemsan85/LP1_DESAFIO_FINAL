from persona import Persona


class Profesional(Persona):
    """Un profesional de salud (medico, enfermero, etc)."""

    def __init__(self, id_persona, dni, nombres, apellidos, especialidad, cargo):
        super().__init__(id_persona, dni, nombres, apellidos)
        self._especialidad = especialidad
        self._cargo = cargo
        self._agenda = []  # 1 profesional -> N citas

    def agregar_cita(self, cita):
        self._agenda.append(cita)

    def get_agenda(self):
        return self._agenda

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo
