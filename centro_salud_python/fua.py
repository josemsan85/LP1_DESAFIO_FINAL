"""Formato Único de Atención (FUA) que se origina a partir de una atención."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from atencion import Atencion


class FUA:
    def __init__(self, id_fua: str, fecha: str, servicio: str, diagnostico: str,
                 procedimiento: str, atencion: Atencion):
        self._id_fua = id_fua
        self._fecha = fecha
        self._servicio = servicio
        self._diagnostico = diagnostico
        self._procedimiento = procedimiento
        self._atencion = atencion  # atención que origina este formato

    @property
    def id_fua(self) -> str:
        return self._id_fua

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def servicio(self) -> str:
        return self._servicio

    @property
    def diagnostico(self) -> str:
        return self._diagnostico

    @property
    def procedimiento(self) -> str:
        return self._procedimiento

    @property
    def atencion(self) -> Atencion:
        return self._atencion
