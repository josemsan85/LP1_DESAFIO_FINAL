class RecetaMedica:
    """Receta medica que se genera a partir de una atencion."""

    def __init__(self, id_receta, fecha, indicaciones, atencion):
        self._id_receta = id_receta
        self._fecha = fecha
        self._medicamentos = []
        self._indicaciones = indicaciones
        self._atencion = atencion  # atencion que origina la receta

    def agregar_medicamento(self, medicamento):
        self._medicamentos.append(medicamento)

    def get_id_receta(self):
        return self._id_receta

    def get_fecha(self):
        return self._fecha

    def get_medicamentos(self):
        return self._medicamentos

    def get_indicaciones(self):
        return self._indicaciones

    def get_atencion(self):
        return self._atencion

    def __str__(self):
        return f"Receta {self._id_receta} ({self._fecha}) - {len(self._medicamentos)} medicamento(s)"
