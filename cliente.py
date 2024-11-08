class Cliente:
    
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Cliente("David", 18)
persona2 = Cliente("Daniel", 18)

print(persona1.nombre, persona1.edad)
print(persona2.nombre, persona2.edad)