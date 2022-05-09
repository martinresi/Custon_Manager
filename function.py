class gim():
    list_clients = []


    def __init__(self):
        pregunta = str(input("desea ingresar datos: si/no: "))

        while pregunta == "si":

            self.nombre = str(input("ingresa el nombre: "))
            apelido = str(input("ingresa el apellido: "))
            dni = int(input("ingresa el DNI: "))
            pregunta = str(input("desea ingresar datos: si/no"))

            list_one = {'nombre': self.nombre, 'apellido': apelido, 'dni': dni}
            self.list_clients.append(list_one)

            if pregunta == "no":
                break

    def show(self, client):
        print(f"{client['nombre']} - {client['apellido']} - {client['dni']}")

    def show_all(self):
        for client in self.list_clients:
            gim.show(self, client)


