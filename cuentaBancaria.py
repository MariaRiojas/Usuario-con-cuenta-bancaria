class cuentaBancaria:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        cuentaBancaria.accounts.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: Cargar $5 fee")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def imprime_todas_cuentas(cls):
        for account in cls.accounts:
            account.mostrar_info_cuenta()


diony = cuentaBancaria(.05,1000)
malory = cuentaBancaria(.02,5000)

diony.deposito(1000).deposito(200).deposito(40).retiro(800).generar_interés().mostrar_info_cuenta()
malory.deposito(3000).deposito(1200).retiro(40).retiro(30).retiro(20).retiro(10).generar_interés().mostrar_info_cuenta()

cuentaBancaria.imprime_todas_cuentas()