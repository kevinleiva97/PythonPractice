class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = str(color)
        self.ruedas = int(ruedas)

    def __str__(self):
        return f'Vehiculo [Color: {self.color}, Numero de ruedas: {self.ruedas}]'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = int(velocidad)

    def __str__(self):
        return f'{super().__str__()}, Coche: [velocidad (kmph): {self.velocidad}]'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = str(tipo)

    def __str__(self):
        return f'{super().__str__()}, Bicicleta: [tipo: {self.tipo}]'


coche1 = Coche('Negro', 4, 80)
bici1 = Bicicleta('Roja', 2, 'Banana')

print('\n \n')
print('Coche'.center(30, '-'))
print(coche1)

print('\n \n')
print('Bicicleta'.center(30, '-'))
print(bici1)
