from turtle import color
from FiguraGeometrica import FiguraGeometrica as FG
from Color import Color as Cl


class Cuadrado(FG, Cl):
    def __init__(self, lado, color):
        # super(FG,Cl).__init__()
        FG.__init__(self, lado, lado)
        Cl.__init__(self, color)

    def CalcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'El Area es de: {self.CalcularArea()}, y los Datos ingresados son: {FG.__str__(self)}'
