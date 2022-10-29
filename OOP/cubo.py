class Cubo:
    def __init__(self, a, p, h):
        self.ancho = int(a)
        self.profundo = int(p)
        self.alto = int(h)

    def calculo(self):
        return self.ancho*self.profundo*self.alto

    def mostrarResultados(self):
        print(f'El resultado del cubo es de: {self.calculo()} mts3')


ancho = input("Ingrese el valor del Ancho: ")
p = input("Ingrese el valor de la profundidad: ")
h = input("Ingrese el valor de la altura: ")

cubo = Cubo(ancho, p, h)
cubo.mostrarResultados()
