class Persona:
    """Clase base para las personas del sistema (pacientes y profesionales)."""

    def __init__(self, id_persona, dni, nombres, apellidos):
        self._id_persona = id_persona
        self._dni = dni
        self._nombres = nombres
        self._apellidos = apellidos

    def get_id_persona(self):
        return self._id_persona

    def set_id_persona(self, id_persona):
        self._id_persona = id_persona

    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        self._dni = dni

    def get_nombres(self):
        return self._nombres

    def set_nombres(self, nombres):
        self._nombres = nombres

    def get_apellidos(self):
        return self._apellidos

    def set_apellidos(self, apellidos):
        self._apellidos = apellidos

    def __str__(self):
        return f"{self._nombres} {self._apellidos} (DNI: {self._dni})"
