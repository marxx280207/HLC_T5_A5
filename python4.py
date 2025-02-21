class cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, sumar):
        self.sumar = sumar
        self.saldo += self.sumar

    def versaldo(self):
        return (f"El saldo es de {self.saldo}")
    
    def retirar(self, restar):
        self.restar = restar
        self.saldo -= self.restar
cuenta = cuenta(3600)
cuenta.depositar(1225)
cuenta.retirar(600)
print(cuenta.versaldo())