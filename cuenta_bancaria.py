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
       return f"""
             nombre: {self.nombre}
             apellido: {self.apellido}
             numero de cuenta: {self.numero_cuenta}
             balance: {self.balance}
             """  
    def depositar(self, valor: int):

        self.balance += valor

    def retirar(self, valor: int):
        self.balance -= valor

def crear_cliente():
    nombre = input("nombre de cliente: ")
    apellido = input("apellido de cliente: ")
    n_cuenta = int(input("numero de cuenta: "))
    balance = int(input("balance: "))

    return {"nombre": nombre, "apellido": apellido, "n_cuenta": n_cuenta, "balance": balance}

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

def validar_retiro(limite):
    cantidad = input("ingrese la cantidad a retirar: ")
    while not cantidad.isnumeric() or int(cantidad) > limite:
        cantidad = input(
            f"por favor ingrese una cantidad en numeros menor a {limite}: ")
    return int(cantidad)

def validar_deposito():
    cantidad = input("ingrese la cantidad a depositar: ")
    while not cantidad.isnumeric() or int(cantidad) < 1:
        cantidad = input("por favor ingrese una cantidad numerica: ")
    return int(cantidad)


def inicio():
    data = crear_cliente()
    system("clear")
    cliente = Cliente(data['nombre'], data['apellido'],
                      data['n_cuenta'], data['balance'])

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
                retiro = validar_retiro(cliente.balance)
                system("clear")
                cliente.retirar(retiro)
                system("clear")
                print(cliente)
                input("oprima enter para continuar ")
                system("clear")

            case 3:
                return

inicio()











