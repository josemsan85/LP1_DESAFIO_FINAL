class FUA:
    """Formulario Unico de Atencion, documento que origina cada atencion."""

    def __init__(self, id_fua, fecha, servicio, diagnostico, procedimiento, atencion):
        self._id_fua = id_fua
        self._fecha = fecha
        self._servicio = servicio
        self._diagnostico = diagnostico
        self._procedimiento = procedimiento
        self._atencion = atencion  # atencion que origina este formato

    def get_id_fua(self):
        return self._id_fua

    def get_fecha(self):
        return self._fecha

    def get_servicio(self):
        return self._servicio

    def get_diagnostico(self):
        return self._diagnostico

    def get_procedimiento(self):
        return self._procedimiento

    def get_atencion(self):
        return self._atencion
