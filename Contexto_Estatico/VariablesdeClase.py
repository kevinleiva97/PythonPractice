class MiClase():
    VariablesClase = 'Valor Variale Clase'

    def __init__(self, variables_instancia):
        self.variables_instancia = variables_instancia


print(MiClase.VariablesClase)

miClase = MiClase('Valor variable Instancia')
print(miClase.variables_instancia)
print(miClase.VariablesClase)

miClase2 = MiClase('otro valor')
print(miClase2.variables_instancia)
print(miClase2.VariablesClase)
