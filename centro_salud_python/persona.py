"""Clase base abstracta de las personas del centro de salud."""
from abc import ABC


class Persona(ABC):
    """Datos comunes de pacientes y profesionales. No se instancia directamente."""

    def __init__(self, id_persona: str, dni: str, nombres: str, apellidos: str):
        # En Java la clase es abstract; aquí se impide instanciarla de forma directa.
        if type(self) is Persona:
            raise TypeError("Persona es abstracta: usa Paciente o Profesional.")
        self._id_persona = id_persona
        self._dni = dni
        self._nombres = nombres
        self._apellidos = apellidos

    @property
    def id_persona(self) -> str:
        return self._id_persona

    @id_persona.setter
    def id_persona(self, valor: str) -> None:
        self._id_persona = valor

    @property
    def dni(self) -> str:
        return self._dni

    @dni.setter
    def dni(self, valor: str) -> None:
        self._dni = valor

    @property
    def nombres(self) -> str:
        return self._nombres

    @nombres.setter
    def nombres(self, valor: str) -> None:
        self._nombres = valor

    @property
    def apellidos(self) -> str:
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor: str) -> None:
        self._apellidos = valor

    def __str__(self) -> str:
        return f"{self._nombres} {self._apellidos} (DNI: {self._dni})"
