class Usuario:
    name_bank="Banco de chile"
    def  __init__(self,name,email_address) -> None:
        self.name =name
        self.email=email_address
        self.balance_cuenta=0
        def hacer_deposito(self, amount):
            self.balance_cuenta +=amount
            return self
        def hacer_retiro(self,other_user):
            self.balance_cuenta = other_user
            return self
        def imprime(self):
            print(f"{self.name}  monto {self.balance_cuenta}" )
            return self
        

        def transferencia(self,amount,user ):
            self.balance_cuenta =amount
            user.balance_cuenta +=amount
            self.imprime()
            user.imprime()
            return self
        

        name="Benjamin"
        email="beng21@gmail.com"
        guido= Usuario(name,email)
        name="Sebastian"
        email="Sebae06@gmail.com"
        monty= Usuario(name,email )
        guido.hacer_deposito(950).hacer_deposito(950).hacer_deposito(950).hacer_deposito(950)
        guido.imprime()
        pass