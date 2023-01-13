# ----------------------------------------------------
# Create a menu driven Phonebook to accept the input
# from the user to add and search for a contact.
# ----------------------------------------------------

# Initialise the variables
varT      = True
sublist   = []
phonebook = []

# Run the loop. Create an outlined structure first.
while varT:
    print("")
    print("        Welcome to the Phonebook        ")
    print("-----------------------------------------")
    print("  PLease choose one of the options below.")
    print("  A - To Add a contact")
    print("  S - To Search a contact")
    print("  E - To Exit the Phonebook")

    option = input("Option : ")
    
    if option == "E":
        varT = False
        
    elif option == "A":
        name    = input("Please enter the name     : ")
        num     = input("Please enter the number   : ")
        email   = input("Please enter the email ID : ")
        
        sublist = [name, num, email]
        
        phonebook.append(sublist)
        print("The contact {} has been added successfully.".format(name))
    
    elif option == "S":
        sname = input("Please enter the name to search for : ")
        found = False
        
        for sublist in phonebook:
            if sname in sublist:
                print("{} is in the phonebook and here are the details.".format(sname))
                print(sublist)
                found = True
        
        if not found:
            print("{} is not found in the phonebook.".format(sname))
    
    else:
        print("Sorry, you have chosen a wrong option.")





















