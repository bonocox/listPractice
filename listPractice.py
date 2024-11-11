list1 = ["Name","Age","Location","telephone"]

def insert ():

    

    name = str(input("Write your name:"))
    age = int(input("How old are you?:"))
    location = str(input("Where are you from?:"))
    telephone = int(input("What's your telephone number?:"))

    list1[0] = name
    list1[1] = age
    list1[2] = location
    list1[3] = telephone

    for index, value in enumerate(list1):
        print(f"The present list is:{index}: {value}")

def update():
    field = int(input("Which field would you like to update? (0-Name, 1-Age, 2-Location, 3-Telephone): "))
    newValue = input("Insert the new information:")
    list1[field] = newValue
    print("Entry updated successfully.")



def delete():
    field = int(input("Which field would you like to delete? (0-Name, 1-Age, 2-Location, 3-Telephone): "))
    list1[field] = None  # Clearing the specific entry
    print("Entry deleted successfully.")



while True:

    

    print("What would you like to do?")
    print("1-Insert.")
    print("2-update.")
    print("3-delete.")
    print("4-show entries.")
    print("5-Exit")


    selection = int(input("Type the corresponding number:"))

    if selection == 1:
        insert()

    elif selection == 2:
        update()

    elif selection == 3:
        delete()

    elif selection == 4:
        for indice, values in enumerate(list1):
            print(f'The saved list contains:{indice}: {values}')

    elif selection == 5:
        print("Exiting the program.")
        break






