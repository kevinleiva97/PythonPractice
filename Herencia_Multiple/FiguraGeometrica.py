# ABC = Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if 0 < ancho < 10:
            self.ancho = ancho
        else:
            self.ancho = 0
        if 0 < alto < 10:
            self.alto = alto
        else:
            self.alto = 0

    @abstractmethod
    def CalcularArea(self):
        pass

    def __str__(self):
        return f'El Alto es de: {self.alto}, y el Ancho es de: {self.ancho}'
