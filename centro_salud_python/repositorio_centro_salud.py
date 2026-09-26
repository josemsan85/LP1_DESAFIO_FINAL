from datetime import date, timedelta

from paciente import Paciente
from profesional import Profesional
from historia_clinica import HistoriaClinica
from atencion import Atencion
from receta_medica import RecetaMedica
from cita import Cita
from fua import FUA


class RepositorioCentroSalud:
    """
    Repositorio central (patron Singleton) que guarda en memoria
    los pacientes, profesionales, atenciones y citas registrados.
    Solo puede existir una instancia en todo el programa.
    """

    _instancia = None

    def __init__(self):
        self._pacientes = []
        self._profesionales = []
        self._atenciones = []
        self._citas = []
        self._fuas = []

        self._contador_paciente = 1
        self._contador_profesional = 1
        self._contador_historia = 1
        self._contador_cita = 1
        self._contador_receta = 1
        self._contador_fua = 1

        self._cargar_datos_de_prueba()

    @staticmethod
    def get_instancia():
        if RepositorioCentroSalud._instancia is None:
            RepositorioCentroSalud._instancia = RepositorioCentroSalud()
        return RepositorioCentroSalud._instancia

    # Datos pre-ingresados para que el sistema no arranque vacio
    def _cargar_datos_de_prueba(self):
        luis = self.crear_paciente("87654321", "Luis", "Ramos Vega", "1990-05-10", "M")
        rosa = self.crear_paciente("71234567", "Rosa", "Chilon Diaz", "1985-02-20", "F")

        ana = self.crear_profesional("27654321", "Ana", "Torres Quispe", "Medicina General", "Medico")
        carlos = self.crear_profesional("29876543", "Carlos", "Mendoza Silva", "Enfermeria", "Enfermero")

        atencion1 = self.crear_atencion(
            luis, ana, str(date.today() - timedelta(days=3)),
            "Dolor de cabeza intenso", "Migraña", "Reposo y analgesico")
        self.crear_receta(
            atencion1, "Tomar con alimentos, reposo 24h",
            ["Paracetamol 500mg - cada 8h por 3 dias"])
        self.crear_fua(atencion1, "Medicina General", "Consulta ambulatoria")

        self.crear_atencion(
            rosa, carlos, str(date.today() - timedelta(days=1)),
            "Control de presion arterial", "Hipertension leve", "Dieta baja en sodio")

        self.crear_cita(luis, ana, str(date.today() + timedelta(days=7)), "10:00")
        self.crear_cita(rosa, carlos, str(date.today() + timedelta(days=10)), "09:30")

    def crear_paciente(self, dni, nombres, apellidos, fecha_nacimiento, sexo):
        id_paciente = f"PA{self._contador_paciente:03d}"
        self._contador_paciente += 1
        paciente = Paciente(id_paciente, dni, nombres, apellidos, fecha_nacimiento, sexo)

        historia = HistoriaClinica(
            f"H{self._contador_historia:03d}", str(date.today()), "Ninguno", "Ninguna", paciente)
        self._contador_historia += 1
        paciente.set_historia_clinica(historia)

        self._pacientes.append(paciente)
        return paciente

    def crear_profesional(self, dni, nombres, apellidos, especialidad, cargo):
        id_profesional = f"PR{self._contador_profesional:03d}"
        self._contador_profesional += 1
        profesional = Profesional(id_profesional, dni, nombres, apellidos, especialidad, cargo)
        self._profesionales.append(profesional)
        return profesional

    def crear_atencion(self, paciente, profesional, fecha, motivo, diagnostico, tratamiento):
        historia = paciente.get_historia_clinica()
        atencion = Atencion(fecha, motivo, diagnostico, tratamiento, profesional, historia)
        historia.agregar_atencion(atencion)
        self._atenciones.append(atencion)
        return atencion

    def crear_receta(self, atencion, indicaciones, medicamentos):
        id_receta = f"REC{self._contador_receta:03d}"
        self._contador_receta += 1
        receta = RecetaMedica(id_receta, str(date.today()), indicaciones, atencion)
        for medicamento in medicamentos:
            receta.agregar_medicamento(medicamento)
        atencion.agregar_receta(receta)
        return receta

    def crear_cita(self, paciente, profesional, fecha, hora):
        id_cita = f"CITA{self._contador_cita:03d}"
        self._contador_cita += 1
        cita = Cita(id_cita, fecha, hora, paciente, profesional)
        paciente.agregar_cita(cita)
        profesional.agregar_cita(cita)
        self._citas.append(cita)
        return cita

    def crear_fua(self, atencion, servicio, procedimiento):
        id_fua = f"FUA{self._contador_fua:03d}"
        self._contador_fua += 1
        fua = FUA(id_fua, atencion.get_fecha(), servicio, atencion.get_diagnostico(),
                  procedimiento, atencion)
        atencion.set_fua(fua)
        self._fuas.append(fua)
        return fua

    def get_pacientes(self):
        return self._pacientes

    def get_profesionales(self):
        return self._profesionales

    def get_atenciones(self):
        return self._atenciones

    def get_citas(self):
        return self._citas

    def get_fuas(self):
        return self._fuas
