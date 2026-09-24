"""Repositorio único (patrón Singleton) con todos los datos del centro de salud."""
from __future__ import annotations

from datetime import date

from atencion import Atencion
from cita import Cita
from historia_clinica import HistoriaClinica
from paciente import Paciente
from profesional import Profesional
from receta_medica import RecetaMedica


class RepositorioCentroSalud:
    _instancia: RepositorioCentroSalud | None = None

    def __init__(self):
        # Usa siempre RepositorioCentroSalud.get_instancia() en lugar de crearlo directamente.
        self._pacientes: list[Paciente] = []
        self._profesionales: list[Profesional] = []
        self._atenciones: list[Atencion] = []
        self._citas: list[Cita] = []

        self._contador_paciente = 1
        self._contador_profesional = 1
        self._contador_historia = 1
        self._contador_cita = 1
        self._contador_receta = 1

    @classmethod
    def get_instancia(cls) -> RepositorioCentroSalud:
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def crear_paciente(self, dni: str, nombres: str, apellidos: str,
                       fecha_nacimiento: str, sexo: str) -> Paciente:
        id_paciente = f"PA{self._contador_paciente:03d}"
        self._contador_paciente += 1
        paciente = Paciente(id_paciente, dni, nombres, apellidos, fecha_nacimiento, sexo)

        historia = HistoriaClinica(f"H{self._contador_historia:03d}",
                                   date.today().isoformat(), "Ninguno", "Ninguna", paciente)
        self._contador_historia += 1
        paciente.historia_clinica = historia

        self._pacientes.append(paciente)
        return paciente

    def crear_profesional(self, dni: str, nombres: str, apellidos: str,
                          especialidad: str, cargo: str) -> Profesional:
        id_profesional = f"PR{self._contador_profesional:03d}"
        self._contador_profesional += 1
        profesional = Profesional(id_profesional, dni, nombres, apellidos, especialidad, cargo)
        self._profesionales.append(profesional)
        return profesional

    def crear_atencion(self, paciente: Paciente, profesional: Profesional, fecha: str,
                       motivo: str, diagnostico: str, tratamiento: str) -> Atencion:
        historia = paciente.historia_clinica
        atencion = Atencion(fecha, motivo, diagnostico, tratamiento, profesional, historia)
        historia.agregar_atencion(atencion)
        self._atenciones.append(atencion)
        return atencion

    def crear_receta(self, atencion: Atencion, indicaciones: str,
                     medicamentos: list[str]) -> RecetaMedica:
        id_receta = f"REC{self._contador_receta:03d}"
        self._contador_receta += 1
        receta = RecetaMedica(id_receta, date.today().isoformat(), indicaciones, atencion)
        for medicamento in medicamentos:
            receta.agregar_medicamento(medicamento)
        atencion.agregar_receta(receta)
        return receta

    def crear_cita(self, paciente: Paciente, profesional: Profesional,
                   fecha: str, hora: str) -> Cita:
        id_cita = f"CITA{self._contador_cita:03d}"
        self._contador_cita += 1
        cita = Cita(id_cita, fecha, hora, paciente, profesional)
        paciente.agregar_cita(cita)
        profesional.agregar_cita(cita)
        self._citas.append(cita)
        return cita

    @property
    def pacientes(self) -> list[Paciente]:
        return list(self._pacientes)

    @property
    def profesionales(self) -> list[Profesional]:
        return list(self._profesionales)

    @property
    def atenciones(self) -> list[Atencion]:
        return list(self._atenciones)

    @property
    def citas(self) -> list[Cita]:
        return list(self._citas)
