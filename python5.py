import math

class figura:
    def __init__(self):
        pass
    def calculararea(self):
        pass
class circulo(figura):
    def __init__(self, radio):
        self.radio = radio
    def calculararea(self):
        return math.pi*self.radio**2
class rectangulo(figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calculararea(self):
        return self.base*self.altura
c = circulo(5)
r = rectangulo(4, 6)
print(c.calculararea())
print(r.calculararea())