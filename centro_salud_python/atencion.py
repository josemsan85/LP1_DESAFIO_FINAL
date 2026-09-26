class Atencion:
    """Una atencion medica: motivo, diagnostico, tratamiento y quien la registro."""

    def __init__(self, fecha, motivo, diagnostico, tratamiento, profesional, historia_clinica):
        self._fecha = fecha
        self._motivo = motivo
        self._diagnostico = diagnostico
        self._tratamiento = tratamiento
        self._profesional = profesional            # quien atiende
        self._historia_clinica = historia_clinica  # a que historia pertenece
        self._fua = None                            # documento generado
        self._recetas = []                          # 1 atencion -> N recetas

    def agregar_receta(self, receta):
        self._recetas.append(receta)

    def get_fecha(self):
        return self._fecha

    def get_motivo(self):
        return self._motivo

    def get_diagnostico(self):
        return self._diagnostico

    def get_tratamiento(self):
        return self._tratamiento

    def get_profesional(self):
        return self._profesional

    def get_historia_clinica(self):
        return self._historia_clinica

    def get_fua(self):
        return self._fua

    def set_fua(self, fua):
        self._fua = fua

    def get_recetas(self):
        return self._recetas
