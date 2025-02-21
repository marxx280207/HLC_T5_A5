class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        return (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}")
    
class trabajador(persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa = empresa

    def presentarse(self):
        return (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y trabajo en {self.empresa}")
p = trabajador('Marc Montoro', 17, 'Butanero', 'Cepsa')
print(p.presentarse())