"""Receta médica generada a partir de una atención."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from atencion import Atencion


class RecetaMedica:
    def __init__(self, id_receta: str, fecha: str, indicaciones: str, atencion: Atencion):
        self._id_receta = id_receta
        self._fecha = fecha
        self._medicamentos: list[str] = []
        self._indicaciones = indicaciones
        self._atencion = atencion  # atención que origina la receta

    def agregar_medicamento(self, medicamento: str) -> None:
        self._medicamentos.append(medicamento)

    @property
    def id_receta(self) -> str:
        return self._id_receta

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def medicamentos(self) -> list[str]:
        return list(self._medicamentos)

    @property
    def indicaciones(self) -> str:
        return self._indicaciones

    @property
    def atencion(self) -> Atencion:
        return self._atencion

    def __str__(self) -> str:
        return f"Receta {self._id_receta} ({self._fecha}) - {len(self._medicamentos)} medicamento(s)"
