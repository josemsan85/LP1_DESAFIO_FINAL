"""Profesional de salud que atiende en el centro."""
from __future__ import annotations

from typing import TYPE_CHECKING

from persona import Persona

if TYPE_CHECKING:
    from cita import Cita


class Profesional(Persona):
    def __init__(self, id_persona: str, dni: str, nombres: str, apellidos: str,
                 especialidad: str, cargo: str):
        super().__init__(id_persona, dni, nombres, apellidos)
        self._especialidad = especialidad
        self._cargo = cargo
        self._agenda: list[Cita] = []  # 1 profesional -> N citas

    def agregar_cita(self, cita: Cita) -> None:
        self._agenda.append(cita)

    @property
    def agenda(self) -> list[Cita]:
        return list(self._agenda)

    @property
    def especialidad(self) -> str:
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor: str) -> None:
        self._especialidad = valor

    @property
    def cargo(self) -> str:
        return self._cargo

    @cargo.setter
    def cargo(self, valor: str) -> None:
        self._cargo = valor
