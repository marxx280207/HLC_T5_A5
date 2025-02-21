class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def presentarse(self):
        return (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}")
p = persona('Marc Montoro', 17, 'Butanero')
print(p.presentarse())