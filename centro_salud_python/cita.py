"""Cita médica entre un paciente y un profesional."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paciente import Paciente
    from profesional import Profesional


class Cita:
    # Estados posibles de una cita
    PENDIENTE = "PENDIENTE"
    ATENDIDA = "ATENDIDA"
    CANCELADA = "CANCELADA"

    def __init__(self, id_cita: str, fecha: str, hora: str,
                 paciente: Paciente, profesional: Profesional):
        self._id_cita = id_cita
        self._fecha = fecha
        self._hora = hora
        self._paciente = paciente
        self._profesional = profesional
        self._estado = Cita.PENDIENTE

    def confirmar_atendida(self) -> None:
        self._estado = Cita.ATENDIDA

    def cancelar(self) -> None:
        self._estado = Cita.CANCELADA

    @property
    def id_cita(self) -> str:
        return self._id_cita

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def hora(self) -> str:
        return self._hora

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @property
    def profesional(self) -> Profesional:
        return self._profesional

    def __str__(self) -> str:
        return (f"Cita {self._id_cita} - {self._paciente.nombres} con {self._profesional.nombres} "
                f"({self._fecha} {self._hora}) [{self._estado}]")
