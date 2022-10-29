from Cuadrado import *
from Rectangulo import *

cuadrado1 = Cuadrado(5, 'Azul')
cuadrado2 = Cuadrado(10, 'Amarillo')
cuadrado3 = Cuadrado(78, 'Morado')
cuadrado4 = Cuadrado(7, 'Negro')

print('\n\n'.center(90, '-'))
print(cuadrado1, '\n', cuadrado2, '\n', cuadrado3, '\n', cuadrado4, '\n')


# MRO Method Resolution Order:
print(Cuadrado.mro())

rec1 = Rectangulo(4, 8, 'Negro')
rec2 = Rectangulo(8, 16, 'Blanco')
rec3 = Rectangulo(2, 50, 'Azul')
rec4 = Rectangulo(1, 8, 'Negro')

print('\n\n'.center(90, '-'))
print(rec1, '\n', rec2, '\n', rec3, '\n', rec4, '\n')
