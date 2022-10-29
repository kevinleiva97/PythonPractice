class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **dic):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = dic

    def mostrarDetalle(self):
        print(
            f'Persona: {self.nombre} {self.apellido}, edad: {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Juan', 'Perez', 28, 2, 3, 5, 7,
                   8, 9, 6, 3, m='Manzana', p='Pera')
persona1.telefono = '55441122'
print(persona1.telefono)
persona2 = Persona('Karla', 'Gomez', 30)


persona1.mostrarDetalle()
persona2.mostrarDetalle()
