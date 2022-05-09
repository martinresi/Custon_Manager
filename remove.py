from function import *


class remove ():
    def exit(self):


        while True:
            print("ingre nombre, apellido, DNI, de la persona a eliminar:")

            nombree=str(input("ingre el nombre de la persona a eliminar:"))
            apellidoo=str(input("ingre el apellido de la persona a eliminar:"))
            DNII=str(input("ingre el DNI de la persona a eliminar:"))

            nombreee = len(gim.list_clients.remove(gim.list_clients[nombree]))
            DNII= len(gim.list_clients.pop(DNII))



            if True != True:
                break





