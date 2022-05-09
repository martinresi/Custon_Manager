from function import *
from remove import *

# importamos estas funciones las cuales nos ayudan a manipular los datos

"""funcion principal"""


def loop():
    gimclass = ''
    exitclass = ''

    while True:

        print("================================")
        print("###### Gestor de Clientes ######")
        print("================================")
        print("[1] Listar Clientes")
        print("[2] Buscar Clientes")
        print("[3] Añadir Clientes")
        print("[4] Modificar Clientes")
        print("[5] Borrar Clientes")
        print("[6] Salir")
        print("================================")

        # ingresamos la opcion
        option = input("")

        if option == "1":
            print("Listando los clientes...\n")

        if option == "2":
            print("Buscar Clientes... \n ")
            if gimclass != '':
                gimclass.show_all()


        if option == "3":
            print("Añadir Clientes... \n ")
            if gimclass == '':
                gimclass=gim()
            else:
                gimclass.__init__()

        if option == "4":
            print("Modificar Clientes... \n ")

        if option == "5":
            print("Borrar Clientes... \n ")
            if exitclass!= '':
                exitclass=remove()
            else:
                exitclass.exit()


        if option == "6":
            print("salir... \n")

            break

        input("\n ENTER para continuar...")


loop()
