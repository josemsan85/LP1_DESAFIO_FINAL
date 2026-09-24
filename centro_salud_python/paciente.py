"""Paciente del centro de salud."""
from __future__ import annotations

from typing import TYPE_CHECKING

from persona import Persona

if TYPE_CHECKING:  # solo para los tipos; evita imports circulares
    from cita import Cita
    from historia_clinica import HistoriaClinica


class Paciente(Persona):
    def __init__(self, id_persona: str, dni: str, nombres: str, apellidos: str,
                 fecha_nacimiento: str, sexo: str):
        super().__init__(id_persona, dni, nombres, apellidos)
        self._fecha_nacimiento = fecha_nacimiento
        self._sexo = sexo
        self._historia_clinica: HistoriaClinica | None = None  # 1 paciente -> 1 historia clínica
        self._citas: list[Cita] = []  # 1 paciente -> N citas

    def agregar_cita(self, cita: Cita) -> None:
        self._citas.append(cita)

    @property
    def citas(self) -> list[Cita]:
        return list(self._citas)  # copia: la lista interna no se expone

    @property
    def fecha_nacimiento(self) -> str:
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor: str) -> None:
        self._fecha_nacimiento = valor

    @property
    def sexo(self) -> str:
        return self._sexo

    @sexo.setter
    def sexo(self, valor: str) -> None:
        self._sexo = valor

    @property
    def historia_clinica(self) -> HistoriaClinica | None:
        return self._historia_clinica

    @historia_clinica.setter
    def historia_clinica(self, valor: HistoriaClinica) -> None:
        self._historia_clinica = valor
