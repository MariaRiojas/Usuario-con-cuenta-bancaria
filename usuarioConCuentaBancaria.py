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

class Usuario:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : cuentaBancaria(.02,1000),
            "savings" : cuentaBancaria(.05,3000)
        }

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Checking Balance: {self.account['checking'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.name}, Savings Balance: {self.account['savings'].mostrar_info_cuenta()}")
        return self

    def transferir_dinero(self,amount,usuario):
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self

maria = Usuario("Maria")
maria.account['checking'].deposito(100)
maria.mostrar_balance_usuario()