from function import *
from remove import *

# import these functions

"""principal function"""


def loop():
    remove_module = Remove()
    gimclass = ''
    exitclass = ''

    while True:

        print("================================")
        print("###### customer manager ######")
        print("================================")
        print("[1] List clients")
        #print("[2] Look for clients")
        print("[2] Add clients")
        #print("[3] Modify clients")
        print("[3] Delate clients")
        print("[4] Exit")
        print("================================")

        # ingresamos la opcion
        option = input("")

        #if option == "1":
            #print("List clients...\n")

        if option == "1":
            print("List clients... \n ")
            if gimclass != '':
                gimclass.show_all()


        if option == "2":
            print("Add clients... \n ")
            if gimclass == '':
                gimclass=gim()
            else:
                gimclass.__init__()

        if option == "3":
            print("Delate clients... \n ")
            remove_module.delete()

        #if option == "4":
            #print("Delate clients... \n ")
            #if exitclass != '':
                #exitclass = Remove()
            #else:
                #exitclass.delete()


        if option == "4":
            print("exit... \n")

            break

        input("\n enter to continue...")


loop()
