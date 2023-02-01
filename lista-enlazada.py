from __future__ import annotations
from dataclasses import dataclass
from nodo import Nodo

@dataclass
class ListaEnlazada():

    # metodos
    # constructor
    def __init__(self):
        self.__primero: Nodo = None
        self.__aux1: Nodo = None
        self.__aux2: Nodo = None
        self.__cantidad: int = 0

    # propiedades
    # getter
    @property
    def primero(self) -> Nodo:
        return self.__primero

    # setter
    @primero.setter
    def primero(self, primero):
        self.__primero = primero

    # getter
    @property
    def aux1(self) -> Nodo:
        return self.__aux1

    # setter
    @aux1.setter
    def aux1(self, aux1):
        self.__aux1 = aux1


    # getter
    @property
    def aux2(self) -> Nodo:
        return self.__aux2

    # setter
    @aux2.setter
    def aux2(self, aux2):
        self.__aux2 = aux2

    # implementacion de algoritmos

    def esta_vacio(self):
        if self.__primero == None:
            return True
        else:
            return False

    def iterar(self):
        foo = self.__primero

        while (foo != None):
            print(f"{foo.informacion}")
            foo = foo.enlace

    # ALGORITMOS DE INSERCION

    def insertar_inicio(self, data: str):

        if self.esta_vacio():
            # crear el primer nodo con su referencia
            self.__primero = Nodo(data)
            self.__primero.enlace = None
        else:
            # hay elementos en la lista
            nuevo = Nodo(data)
            nuevo.enlace = self.__primero
            self.__primero = nuevo

        self.__cantidad = self.__cantidad + 1

    def insertar_final(self, data: str):

        if self.esta_vacio():
            # crear el primer nodo con su referencia
            self.__primero = Nodo(data)
            self.__primero.enlace = None
        else:
            aux1 = self.__primero

            while aux1.enlace != None:
                aux1 = aux1.enlace

            nuevo = Nodo(data)
            nuevo.enlace = None
            aux1.enlace = nuevo
            axu1 = nuevo

        self.__cantidad = self.__cantidad + 1


    def insertar_antes_de_x(self, data, referencia):

        nuevo = self.__primero
        band = True

        while (nuevo.informacion != referencia and band):

            if nuevo.enlace != None:
                aux1 = nuevo
                nuevo = nuevo.enlace
            else:
                band = False

        if band:

            nodo_insertar_antes = Nodo(data)

            if self.__primero == nuevo:
                nodo_insertar_antes.enlace = self.__primero
                self.__primero = nodo_insertar_antes
            else:
                aux1.enlace = nodo_insertar_antes
                nodo_insertar_antes.enlace = nuevo

            self.__cantidad = self.__cantidad + 1

        else:
            print("El nodo dado como referencia no existe en la lista")
     

lista = ListaEnlazada()

lista.insertar_inicio("Hollmann")
lista.insertar_inicio("Ivan")
lista.insertar_inicio("Keyling")
lista.insertar_inicio("Jaime")

lista.insertar_final("Wilmer")
lista.insertar_final("Osman")

lista.insertar_antes_de_x("Oscar", "Jaime")

print(f"\nEste es el primer nodo: {lista.primero.informacion}")

lista.iterar()






            




        







    






    


    
    
