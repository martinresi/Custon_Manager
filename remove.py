from function import *


class Remove ():
    def buscar_por_nombre(self, name):
        for indice, cliente in enumerate(gim.list_clients):
            if cliente['name'] == name:
                return indice

        return None


    def delete(self):

        print("Enter name, surname, ID, of the person to delete:")

        namee=str(input("enter the name of the person to delete:"))
        last_namee=str(input("enter the last name of the person to delete:"))
        idd=str(input("Enter the ID of the person to be deleted:"))

        indice_de_lista = self.buscar_por_nombre(namee)
        if indice_de_lista != None:
            cliente = gim.list_clients.pop(indice_de_lista)
            print(f"The following customer has been removed {str(cliente)}")
        else:
            print("The client to delete was not found")

