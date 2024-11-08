class Cliente:
    
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Cliente("David", 18)
print(persona1.nombre, persona1.edad)