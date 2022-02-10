class Usuario:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def hacer_deposito(self, amount):
        self.amount += amount
        return self

    def mostrar_balance_usuario(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def hacer_retiro(self,amount):
        self.amount -= amount
        return self

    def transferir_dinero(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_balance_usuario()
        user.mostrar_balance_usuario()
        return self

maria = Usuario("Maria")
sofia = Usuario("Sofia")
naomi = Usuario("Naomi")

maria.hacer_deposito(300).hacer_deposito(400).hacer_deposito(20).hacer_retiro(25).mostrar_balance_usuario()

sofia.hacer_deposito(980).hacer_deposito(900).hacer_retiro(300).hacer_retiro(200).mostrar_balance_usuario()

naomi.hacer_deposito(2000).hacer_retiro(800).hacer_retiro(200).hacer_retiro(60).mostrar_balance_usuario()

sofia.transferir_dinero(40, naomi)