from get_y_set import Persona
print("Creacion de Objetos".center(35, '-'))
persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)

print(__name__)

print('Eliminacion de Objetos'.center(30, '-'))
del persona1
