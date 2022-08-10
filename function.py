class gim():
    list_clients = []


    def __init__(self):
        Question = str(input("want to enter data: yes/no: "))

        while Question == "yes":

            self.name = str(input("enter name: "))
            last_Name = str(input("enter last name: "))
            id = int(input("enter DNI: "))
            Question = str(input("want to enter data: yes/no: "))

            list_one = {'name': self.name, 'last_name': last_Name, 'ID': id}
            self.list_clients.append(list_one)

            if Question == "no":
                break

    def show(self, client):
        print(f"{client['name']} - {client['last_name']} - {client['ID']}")

    def show_all(self):
        for client in self.list_clients:
            gim.show(self, client)


