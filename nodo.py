from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Nodo:

    # Metodos
    
    # metodo constructor
    # __nombre__ => metodos magicos
    def __init__(self, informacion: str) -> None:
        self.__informacion: str = informacion
        self.__enlace: Nodo = None

    # metodo equal
    def __eq__(self, value):
        if not isinstance(value, Nodo):
            return NotImplemented

        return self.__informacion == value.informacion and self.__enlace == value.enlace

    # propiedades

    # getter
    @property
    def informacion(self) -> str:
        return self.__informacion

    # setter
    @informacion.setter
    def informacion(self, informacion: str):
        self.__informacion = informacion

    # getter
    @property
    def enlace(self) -> Nodo:
        return self.__enlace

    # setter
    @enlace.setter
    def enlace(self, enlace: Nodo):
        self.__enlace = enlace
    
