"""Historia clínica de un paciente."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from atencion import Atencion
    from paciente import Paciente


class HistoriaClinica:
    def __init__(self, id_historia: str, fecha_apertura: str, antecedentes: str,
                 alergias: str, paciente: Paciente):
        self._id_historia = id_historia
        self._fecha_apertura = fecha_apertura
        self._antecedentes = antecedentes
        self._alergias = alergias
        self._paciente = paciente  # dueño de la historia
        self._atenciones: list[Atencion] = []  # 1 historia -> N atenciones

    def agregar_atencion(self, atencion: Atencion) -> None:
        self._atenciones.append(atencion)

    @property
    def id_historia(self) -> str:
        return self._id_historia

    @property
    def fecha_apertura(self) -> str:
        return self._fecha_apertura

    @property
    def antecedentes(self) -> str:
        return self._antecedentes

    @property
    def alergias(self) -> str:
        return self._alergias

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @property
    def atenciones(self) -> list[Atencion]:
        return list(self._atenciones)
