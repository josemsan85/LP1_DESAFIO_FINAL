class HistoriaClinica:
    """La historia clinica de un paciente. Guarda todas sus atenciones."""

    def __init__(self, id_historia, fecha_apertura, antecedentes, alergias, paciente):
        self._id_historia = id_historia
        self._fecha_apertura = fecha_apertura
        self._antecedentes = antecedentes
        self._alergias = alergias
        self._paciente = paciente          # dueño de la historia
        self._atenciones = []              # 1 historia -> N atenciones

    def agregar_atencion(self, atencion):
        self._atenciones.append(atencion)

    def get_id_historia(self):
        return self._id_historia

    def get_fecha_apertura(self):
        return self._fecha_apertura

    def get_antecedentes(self):
        return self._antecedentes

    def get_alergias(self):
        return self._alergias

    def get_paciente(self):
        return self._paciente

    def get_atenciones(self):
        return self._atenciones
