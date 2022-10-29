from FiguraGeometrica import FiguraGeometrica as FG
from Color import Color as Cl


class Rectangulo(FG, Cl):
    def __init__(self, ancho, largo, color):
        FG.__init__(self, ancho, largo)
        Cl.__init__(self, color)

    def CalcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'El Area del Rectangulo es de: {self.CalcularArea()} y sus datos son: {FG.__str__(self)}'
