class AreaRectangulo:
    def __init__(self, b, h):
        self.base = b
        self.altura = h

    def calculoArea(self):
        return self.base * self.altura

    def mostrarResultados(self):
        print(f'el resultado del area del triangulo es: {self.calculoArea()}')


base = int(input("Proporcione la Base: "))
altura = int(input("Proporcione la Altura: "))

area = AreaRectangulo(base, altura)
area.mostrarResultados()
