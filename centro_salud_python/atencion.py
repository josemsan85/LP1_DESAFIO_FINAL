"""Atención médica registrada en una historia clínica."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fua import FUA
    from historia_clinica import HistoriaClinica
    from profesional import Profesional
    from receta_medica import RecetaMedica


class Atencion:
    def __init__(self, fecha: str, motivo: str, diagnostico: str, tratamiento: str,
                 profesional: Profesional, historia_clinica: HistoriaClinica):
        self._fecha = fecha
        self._motivo = motivo
        self._diagnostico = diagnostico
        self._tratamiento = tratamiento
        self._profesional = profesional  # quien atiende
        self._historia_clinica = historia_clinica  # a qué historia pertenece
        self._fua: FUA | None = None  # documento generado
        self._recetas: list[RecetaMedica] = []  # 1 atención -> N recetas

    def agregar_receta(self, receta: RecetaMedica) -> None:
        self._recetas.append(receta)

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def motivo(self) -> str:
        return self._motivo

    @property
    def diagnostico(self) -> str:
        return self._diagnostico

    @property
    def tratamiento(self) -> str:
        return self._tratamiento

    @property
    def profesional(self) -> Profesional:
        return self._profesional

    @property
    def historia_clinica(self) -> HistoriaClinica:
        return self._historia_clinica

    @property
    def fua(self) -> FUA | None:
        return self._fua

    @fua.setter
    def fua(self, valor: FUA) -> None:
        self._fua = valor

    @property
    def recetas(self) -> list[RecetaMedica]:
        return list(self._recetas)

    def __str__(self) -> str:
        return f"{self._fecha} - {self._diagnostico} ({self._profesional.nombres})"
