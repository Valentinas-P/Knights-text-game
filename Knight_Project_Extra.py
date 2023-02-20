import random

############################################################
#                                                          #
#                                                          #
#                        (>Knight-SW<)                     #
#                                             Valentinas.P #
#                                             25/01/2023   #
############################################################

print("############################################################")
print("#                                                          #")
print("#                                                          #")
print("#             Welcome to --- (>Knight-SW GAME!<)           #")
print("#                                                          #")
print("#                                                          #")
print("############################################################\n")


# It checks error handing by using try and except method. Firstly it takes from the user input, then it checks if the input is numerical value e,g. "5"
# If the input is numerical it raises an error handler ValueError. If the input is string it skips the if statement and continues to adding a string (name) to the knigts list value.
# And prints the results using  formatted string literal to the user.
# -------- A function to create a knight ----------->
def create_kinght(knights):
    # checks
    try:
        name = input("What is the knights name: ")
        if name.isdigit():
            raise ValueError
        # Adds the information to the knights list
        knights.append([name])
        print(f"You have created a knight called: {name}")
    except ValueError:
        print("Please enter a string value, not a number!")


#This code creates a function "create_class" which takes a list "knights_class" as input. 
# The function then prompts the user to enter a name for a new knight class and adds the name to the "knights_class" list. 
# If the user enters a number instead of a string, the function raises a "ValueError" exception and prints an error message "Please enter a string value, not a number!".
# -------- A function to create a knight class ----------->
def create_class(knights_class):
    try:
        name = input("What is the knights class name: ")
        if name.isdigit():
            raise ValueError
        # Adds the information to the knights_class list
        knights_class.append([name])
        print(f"You have created a knight class: {name}")
    except ValueError:
        print("Please enter a string value, not a number!")


# This code creates a function "create_weapon" which takes a list "weapon" as input.
# The function then prompts the user to enter a name for a new weapon and adds the name to the "weapon" list.
# If the user enters a number instead of a string, the function raises a "ValueError" exception and prints an error message "Please enter a string value, not a number!".
# -------- A function to create a weapon ----------->
def create_weapon(weapon):
    try:
        name = input(str("What is your weapon name?: "))
        if name.isdigit():
            raise ValueError
        # Adds the information to the weapon list
        weapon.append([name])
        print(f"You have created: {name} weapon")
    except ValueError:
        print("Please enter a string value, not a number!")


#This code defines a function "change_data" which takes a list "knights" as input. 
# The function displays the current name of the knight stored in the "knights" list and prompts the user to select an option to update. 
# If the user selects option 1, the function prompts the user to enter the new name for the knight. 
# If the user inputs a number instead of a string, the function raises a "ValueError" exception and prints an error message "Please enter a string value, not a number!". 
# If the user inputs anything other than 1, the function displays an error message "Please select a valid option". 
# If the user input is not a number, the function raises an exception and prints an error message "Try Again!". 
# The function then calls itself recursively.
# -------- A function to change the knight name ----------->
def change_data(knights):
    print("\n--- What would you like to update? ---")
    print(f"1: Knights name: {knights[0]}")
    try:
        selection = int(input("Seleciton your option: "))
        if selection == 1:
            try:
                k_data = input("What is the new knights' name?: ")
                if k_data.isdigit():
                    raise ValueError
                else:
                    knights[0] = k_data
                    print(f"Your knights new name is: {knights[0]}\n")
            except ValueError:
                print("Please enter a string value, not a number!")
                change_data(knights)
        else:
            print("--- Please select a valid option ---")
    except:
        print("--- Try Again! ---")
        change_data(knights)


# This code defines a function "change_class_data" which takes a list "knights_class" as input. 
# The function displays the current name of the knight stored in the "knights_class" list and prompts the user to select an option to update. 
# If the user selects option 1, the function prompts the user to enter the new name for the knight.
#  If the user inputs a number instead of a string, the function raises a "ValueError" exception and prints an error message "Please enter a string value, not a number!".
#  If the user inputs anything other than 1, the function displays an error message "Please select a valid option". 
# If the user input is not a number, the function raises an exception and prints an error message "Try Again!". 
# The function then calls itself recursively.
# -------- A function to change the current's knight class name ----------->
def change_class_data(knights_class):
    print("\n--- What would you like to update? ---")
    print(f"1. Knights class name: {knights_class[0]}")
    try:
        selection = int(input("Select your option: "))
        if selection == 1:
            try:
                class_data = input("What is the new knight's class name?: ")
                if class_data.isdigit():
                    raise ValueError
                else:
                    knights_class[0] = class_data
                    print(f"Your knights class new name is: {knights_class[0]}\n")
            except ValueError:
                print("Please enter a string value, not a number!")
                change_class_data(knights_class)
        else:
            print("--- Please select a valid option ---")
    except:
        print("--- Try Again! ---")
        change_class_data(knights_class)


# -------- A function to change the weapons name from the list ----------->
def change_weapons_data(knights_weapon):
    print("\n--- What weapon would you like to update from the list? ---")
    print(f"1. Knights weapon name: {knights_weapon[0]}")
    try:
        selection = int(input("Select your option: "))
        if selection == 1:
            try:
                weapon = input("What is the new weapon's name?: ")
                if weapon.isdigit():
                    raise ValueError
                else:
                    knights_weapon[0] = weapon
                    print(f"Your new weapon name is: {knights_weapon[0]}\n")
            except ValueError:
                print("Please enter a string value, not a number!")
                change_weapons_data(knights_weapon)
        else:
            print("--- Please select a valid option ---")
    except:
        print("--- Try Again! ---")
        change_weapons_data(knights_weapon)


# This code defines a function "select_knight" which takes a list "knights" as input. 
# The function displays a list of knight names with their corresponding number stored in the "knights" list. 
# The user is prompted to select a knight by number. The function then calls the "change_data" function with the selected knight's information as input. 
# The "change_data" function is expected to modify the selected knight's information.
# -------- A function to show the current knights that the user have in the list, more than one ----------->
def select_knight(knights):
    print("What Knight would you like to update?\n")
    for i, knight in enumerate(knights, start=1):
        print(f"{i}-> Knights name: {knight[0]}")
    selection = int(input("\nSelect the Knights number: ")) - 1
    change_data(knights[selection])


# -------- A function to show the current knights class that the user chosen ----------->
def select_class(knights_class):
    print("What Knight class would you like to update?\n")
    for i, knight_class in enumerate(knights_class, 1):
        print(f"{i} -> Knights class name: {knight_class[0]}")
    selection = int(input("\nSelect the Knights class number: ")) - 1
    change_class_data(knights_class[selection])


# -------- A function to show the current knights class that the user chosen ----------->
def select_weapon(knights_weapon):
    print("What weapon would you like to update?\n")
    for i, knight_weapon in enumerate(knights_weapon, 1):
        print(f"{i} -> Knights weapon name: {knight_weapon[0]}")
    selection = int(input("\nSelect the weapon number: ")) - 1
    change_weapons_data(knights_weapon[selection])


# -------- A function to check if user have knights or class 
# -------- and prints out the current knights and classes the user have.
def display_knights_and_classes(knights, knights_class):
    if not knights:  # if knights equal to 0 then:
        print("Wait... You have no knights & class! Have a number: " + str(random.randint(0, 100)))
        return print("\n")  # Returns with a new line
    countries = [["United States","China","Brazil",
                    "Japan","Russia","Mexico"],
                    ["Turkey","Thailand","Egypt",
                    "Germany","France","United Kingdom"]
                ]
# This code creates a list "countries" with two sublists, each containing six countries.
# It then uses the "random.choice" function from the "random" module to randomly select one of the sublists and store it in the variable "random_list".
# It then uses the "random.choice" function again to randomly select one of the countries from the selected sublist and store it in the variable "random_country".
    random_list = random.choice(countries)
    random_country = random.choice(random_list)
    print("--- All your Knights & selected options! ---\n")
    for i, knight in enumerate(knights):
        print(f"{i+1}-- Knight's name: {knight[i][0]} -- class {i}: {knights_class[i][0]} -- weapon {i+1}: {knight_weapon[i][0]} -- country: {random_country}")


# -------- A function to show the main menu to the user ----------->
def menu(knights_number):
    # Print the current options
    print("\nWhat do you want to do?\n1: Create a new knight\n2: Update your knight\n3: Create knights class\n4: Update your knight class\n5: Create a weapon\n6: Update weapon\n0: Exit the program\n")
    # Allow selection to be tested
    try:
        # Takes the users input selection
        selection = int(input("Selection number: "))
        #Create a new knight
        if selection == 1:
            create_kinght(knights)
            # Print out the knight that was made
            print("\n--- Your Knight ---\nKnight's name: ",knights[knights_number][0])
            knights_number += 1
            menu(knights_number)

            # Updates the information of the knight
        elif selection == 2:
            if not knights:
                print("You need to create a Knight first!\n")
            else:
                select_knight(knights)
                menu(knights_number)

        # Create a class for the knight
        elif selection == 3:
            create_class(knights_class)
            # Print out the knights class that was made
            print("\n--- Your knight class ---\nKnights class name: ",knights_class[knights_number][0])
            knights_number += 1
            menu(knights_number)

        # Update a knights class
        elif selection == 4:
            if not knights_class:  # if knights_class is empty then:
                print("You need to create a Knights Class first!\n")
            else:
                select_class(knights_class)
            menu(knights_number)

        # Create a weapon for the user if the user typed "5"
        elif selection == 5:
            create_weapon(knight_weapon)
            # Print out the knights weapon
            print("\n--- Your weapon inventory ---\nWeapons name: ",knight_weapon[knights_number][0])
            knights_number += 1
            menu(knights_number)

        # Update a weapon if the user already has created a weapon
        elif selection == 6:
            if not knight_weapon:
                print("You need to create a weapon first!\n")
            else:
                select_weapon(knight_weapon)
            menu(knights_number)

        # If input is typed as ("0 -> zero") then call the display_knights_and_classes function.
        elif selection == 0:
            display_knights_and_classes(knights, knights_class)
            print("\n")
        # Required for catching integar number
        else:
            print("--- Try Again! ---\n")
            menu(knights_number)
        # We are looking for integar number selection
    except:
        print("--- Try Again! ---\n")
        menu(knights_number)


# -------- Setting the scene for the user ----------->
knights_number = 0
knights_class_n = 0
knights = []
knights_class = []
knight_weapon = []
# -------- Run the program ----------->
menu(knights_number)