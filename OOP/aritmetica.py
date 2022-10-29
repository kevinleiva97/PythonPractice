class Aritmetica:
    """
    clase artimetica para realizar las operaciones basicas (+-*/)
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def suma(self):
        return self.operandoA+self.operandoB

    def resta(self):
        return self.operandoA-self.operandoB

    def multiplicacion(self):
        return self.operandoA*self.operandoB

    def division(self):
        return self.operandoA/self.operandoB


suma = Aritmetica(1, 2)
print(suma.suma())

res = Aritmetica(1, 2)
print(res.resta())

mult = Aritmetica(2, 2)
print(mult.multiplicacion())

div = Aritmetica(10, 2)
print(div.division())
