from function import *


class remove ():
    def buscar_por_nombre(self, nombre):
        for indice, cliente in enumerate(gim.list_clients):
            if cliente['nombre'] == nombre:
                return indice

        return None


    def delete(self):

        print("ingre nombre, apellido, DNI, de la persona a eliminar:")

        nombree=str(input("ingre el nombre de la persona a eliminar:"))
        apellidoo=str(input("ingre el apellido de la persona a eliminar:"))
        DNII=str(input("ingre el DNI de la persona a eliminar:"))

        indice_de_lista = self.buscar_por_nombre(nombree)
        if indice_de_lista != None:
            cliente = gim.list_clients.pop(indice_de_lista)
            print(f"Se ha eliminado el siguiente cliente {str(cliente)}")
        else:
            print("No se encontro el cliente a eliminar")

