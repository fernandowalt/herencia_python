from os import system


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"nombre: {self.nombre}\napellido: {self.apellido}\nnumero de cuenta: {self.numero_cuenta}\nbalance: {self.balance}\n"

    def depositar(self, valor: int):

        self.balance += valor

    def retirar(self, valor: int):

        if self.balance >= valor:
            self.balance -= valor

            return True
        else:
            return False


def crear_cliente():
    nombre = input("nombre de cliente: ")
    apellido = input("apellido de cliente: ")
    n_cuenta = int(input("numero de cuenta: "))
    balance = int(input("balance: "))
    cliente = Cliente(nombre, apellido, n_cuenta, balance)

    return cliente


def validar_opcion():

    respuesta = input(f"""
                   =========Cuenta bancaria=========

                   1.Depositar
                   2.Retirar
                   3.salir

                    """)
    while not respuesta.isnumeric() or int(respuesta) not in range(1, 4):
        respuesta = input(f"por favor elige una opción valida (1-3: ")
    return int(respuesta)


def validar_retiro():

    cantidad = input("ingrese la cantidad a retirar: ")
    while not cantidad.isnumeric():
        cantidad = input(f"por favor ingrese una cantidad en numeros")

    return int(cantidad)


def validar_deposito():

    cantidad = input("ingrese la cantidad a depositar: ")
    while not cantidad.isnumeric():
        cantidad = input("por favor ingrese una cantidad en numeros: ")
    return int(cantidad)


def inicio():
    cliente = crear_cliente()
    system("clear")

    opcion = 1
    while opcion in range(1, 3):
        opcion = validar_opcion()
        system("clear")

        match opcion:

            case 1:
                deposito = validar_deposito()
                system("clear")
                cliente.depositar(deposito)
                system("clear")
                print(cliente)
                input("oprima enter para continuar: ")
                system("clear")

            case 2:
                retiro = validar_retiro()
                system("clear")
                resultado = cliente.retirar(retiro)
                if resultado:
                    print("retiro realizado\n")
                    print(cliente)
                    input("presione enter para continuar")
                    system("clear")
                else:
                    print("fondos insuficientes\n")
                    print(cliente)
                    input("presione enter para continuar")
                    system("clear")

            case 3:
                return


inicio()
