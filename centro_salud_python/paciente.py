from persona import Persona


class Paciente(Persona):
    """Un paciente del centro de salud. Hereda datos generales de Persona."""

    def __init__(self, id_persona, dni, nombres, apellidos, fecha_nacimiento, sexo):
        super().__init__(id_persona, dni, nombres, apellidos)
        self._fecha_nacimiento = fecha_nacimiento
        self._sexo = sexo
        self._historia_clinica = None  # 1 paciente -> 1 historia clinica
        self._citas = []               # 1 paciente -> N citas

    def agregar_cita(self, cita):
        self._citas.append(cita)

    def get_citas(self):
        return self._citas

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def get_sexo(self):
        return self._sexo

    def set_sexo(self, sexo):
        self._sexo = sexo

    def get_historia_clinica(self):
        return self._historia_clinica

    def set_historia_clinica(self, historia_clinica):
        self._historia_clinica = historia_clinica
