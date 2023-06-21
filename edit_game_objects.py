# ----------------------------------------------------------------------------#
# Title: My Hero - Manage Game Objects
# Description: Code to manage game objects used in My Hero:
#   Hero, Monster, Weapon, Potion, Spell

# Change Log
# AFolmer, 2023.06.21, Created initial script
# Program to manage lists of object classes Character (player, monster) and Item (weapon, potion, spell) for use
# in My Hero game
# Goals for next release:
# Update functions from printing object properties as strings to printing formatted tables
# Convert static methods within classes to shared IO where possible
# Add check to see if Item/Character is already in list to "add object"
# ----------------------------------------------------------------------------#

# Import pickle functionality to save our lists of objects
import pickle


# Base class for players and monsters
class Character(object):
    def __init__(self, char_type, name, desc, life, dex):
        """Create a new hero or monster using the Constructor function __init__
        :param char_type: character type - player or monster (str)
        :param name: character name, name of hero or monster (str)
        :param desc: character description, description of hero or monster
        :param life: character life, hit points
        :param dex: character dexterity, chance to dodge or critical hit"""
        self.char_type = char_type
        self.name = name
        self.desc = desc
        self.life = life
        self.dex = dex

    def __repr__(self):
        """Creates a string representing the Character object
        :return: string representing object"""
        return f'{self.char_type.capitalize()}: {self.name.capitalize()}'

    @staticmethod
    def edit_char_type(self):
        """Capture user input for character type
        :return char_type: string with character type"""
        print("Character Type: 1 = Player, 2 = Monster")
        char_type_choice = IO.input_integer_choice(2)
        if char_type_choice == 1:
            char_type = "Player"
        else:
            char_type = "Monster"
        return char_type

    @staticmethod
    def char_in_inventory(name):
        """Check to see if user entered character name is in inventory and return list index
        :param name: name of the character
        :return in_inventory: is character in list, True/False
        :return char_index: character index in inventory"""
        in_inventory = False
        char_index = 0
        # Loop to go through the list and check if user entered name matches object attribute name
        for i in list_character_objects:
            # Break the loop if the user entered name matches an object name
            if i.name == name:
                in_inventory = True
                break
            else:
                char_index += 1
        return in_inventory, char_index

    @staticmethod
    def print_character_list(self):
        """Print a list of players and a list of monsters.  Update strings to formatted table in next release."""
        # For/if loop to print all Characters with the parameter Player
        print("Players")
        for char_index in list_character_objects:
            if char_index.char_type == "Player":
                print(char_index.name.capitalize() + ": " + char_index.desc + " Life: " + str(char_index.life)
                      + " Dexterity: " + str(char_index.dex))
        # For/if loop to print all Characters with the parameter Monster
        print("Monsters")
        for char_index in list_character_objects:
            if char_index.char_type == "Monster":
                print(char_index.name.capitalize() + ": " + char_index.desc + ". Life: " + str(char_index.life)
                      + " Dexterity: " + str(char_index.dex))


# Base class for objects in character inventory
class Item(object):
    def __init__(self, item_type, name, desc, attack, defend, heal, value):
        """Create an item available to hero or monster using the Contstructor class __init__
        :param item_type: item type - weapon, potion, or spell
        :param name: item name (str)
        :param desc: item description (str)
        :param attack: points damage dealt (int)
        :param defend: points damage prevented (int)
        :param heal: points healed (int)
        :param value: money to buy/sell (int)"""
        self.item_type = item_type
        self.name = name
        self.desc = desc
        self.attack = attack
        self.defend = defend
        self.heal = heal
        self.value = value

    def __repr__(self):
        """Creates a string representing item object
        :return: string representing object"""
        return f'{self.item_type.captialize()}: {self.name.capitalize()}'

    @staticmethod
    def enter_item_type(self):
        """Capture user input for item type
        :return item_type: string with item type"""
        # Function input_integer_choice to capture choice 1 - 3
        print("Item Type: 1 = Weapon, 2 = Potion, 3 = Spell")
        item_type_choice = IO.input_integer_choice(3)
        if item_type_choice == 1:
            item_type = "Weapon"
        elif item_type_choice == 2:
            item_type = "Potion"
        else:
            item_type = "Spell"
        return item_type

    @staticmethod
    def item_in_inventory(name):
        """Check to see if user entered item name is in inventory and return list index
        :param name: name of the item
        :return in_inventory: is item in list, True/False
        :return item_index: item index in inventory"""
        in_inventory = False
        item_index = 0
        # Go through list of item objects to see if the user entered name matches object attribute name
        for i in list_item_objects:
            if i.name == name:
                in_inventory = True
                break
            else:
                item_index += 1
        return in_inventory, item_index

    @staticmethod
    def print_item_list(self):
        """Print lists of weapons, potions, and spells.  Update strings to formatted table in next release."""
        # For/if loop to print all Items with the parameter Weapon
        print("Weapons")
        for item_index in list_item_objects:
            stat_string = f'Attack: {str(item_index.attack)} Defend: {str(item_index.defend)}'
            if item_index.item_type == "Weapon":
                print(item_index.name.capitalize() + " : " + item_index.desc.capitalize() + stat_string)
        # For/if loop to print all Items with the parameter Potion
        print("Potions")
        for item_index in list_item_objects:
            stat_string = f'Attack: {str(item_index.attack)} Defend: {str(item_index.defend)}'
            if item_index.item_type == "Potion":
                print(item_index.name.capitalize() + " : " + item_index.desc.capitalize() + stat_string)
        # For/if loop to print all Items with the parameter Spell
        print("Spells")
        for item_index in list_item_objects:
            stat_string = f'Attack: {str(item_index.attack)} Defend: {str(item_index.defend)}'
            if item_index.item_type == "Spell":
                print(item_index.name.capitalize() + " : " + item_index.desc.capitalize() + stat_string)

# Presentation (Input/Output -----------------------------------------------#
# Functions to print text used by both classes and capture user choices for integers and strings, then validate
# inputs meet parameter requirements e.g. max string length, max integer value
class IO:
    @staticmethod
    def main_menu():
        """Print main menu of choices for user
        :return: nothing"""
        # Print statement broken into two lines for ease in reading code
        print("Main Menu \n1. Edit characters: Players and Monsters \n2. Edit items: Weapons, Potions, and Spells")
        print("3. Save game data to file \n4. Exit program")

    @staticmethod
    def sub_menu(menu_choice):
        """Print sub menu of choices for user
        :return: nothing"""
        # Object list being edited
        if menu_choice == 1:
            print("Heroes & Monsters")
        else:
            print("Weapons, Potions, and Spells")
        print("1. View \n2. Add \n3. Edit \n4. Delete \n5. Main Menu")

    @staticmethod
    def input_integer_choice(upper):
        """Captures and validates user entered menu choice
        :param upper: the highest menu option
        :return user_choice: valid user choice"""
        while True:
            # Try/ except to ensure user enters an integer
            try:
                user_choice = int(input("Enter value between 1 and " + str(upper) + " "))
            except ValueError:
                print("Choice must be an integer between 1 and " + str(upper))
            except:
                print("Unknown error")
            # If user meets requirements, break loop and return value
            else:
                if 0 < user_choice <= upper:
                    break
                # Notify user and try again if integer does not meet value requirement
                else:
                    print("Choice must be an integer between 1 and " + str(upper))
        return user_choice

    @staticmethod
    def input_str_choice(upper):
        """Captures and validates user entered string
        :param upper: max number of characters in string
        :return user_string: string meeting length requirements"""
        # While loop executed until user enters a string below max length
        while True:
            # Try except to ensure user enters a string
            try:
                user_string = input("Max characters " + str(upper) + " ")
            except ValueError:
                print("Must be a string.")
            except:
                print("Invalid entry.")
            else:
                # Check length and convert valid entry to lower case
                user_string = user_string.lower()
                if 0 < len(user_string) <= upper:
                    break
                # Notify user and try again if string does not meet length requirement
                else:
                    print("Must be 1 - " + str(upper) + " characters.")
        return user_string


# Main body of script ------------------------------------------------------#
# Variables to capture user choices to navigate program
main_menu_choice = 0  # Main menu choice
max_main_choice = 4  # Highest value main menu choice
sub_menu_choice = 0  # Sub-menu choice
max_sub_choice = 5  # Highest value sub-menu choice
max_name_len = 25  # Max name length
max_desc_len = 50  # Max description length
max_stat = 20  # Max value for life, attack, defend,

# Try to open pickle file with lists of characters and items
try:
    f = open("my_hero_objects.dat", "rb")
    list_character_objects = pickle.load(f)
    list_item_objects = pickle.load(f)
    f.close()
# Create lists for characters and items if pickle does not load
except:
    list_character_objects = []
    list_item_objects = []
# While loop executes menu choices until user exits
while True:
    # Display main menu
    IO.main_menu()
    # Function input integer choice validates menu choice is integer 1 - 4
    main_menu_choice = IO.input_integer_choice(max_main_choice)
    # Code block for user to view, add, edit, and delete characters
    if main_menu_choice == 1:
        # User loops through character sub menu until they select 5 to exit to main menu
        while True:
            IO.sub_menu(main_menu_choice)
            sub_menu_choice = IO.input_integer_choice(max_sub_choice)
            # Print all players and monsters; update to proper formatted table in next release
            if sub_menu_choice == 1:
                # Notify user if list is empty
                if len(list_character_objects) == 0:
                    print("Your character list is empty.")
                else:
                    # Function to print a list of player characters and a list of monster characters
                    Character.print_character_list(self=1)
            # Add a new object with the class Character
            elif sub_menu_choice == 2:
                # Functions input str choice and input integer choice used to ensure that user enters valid values
                # for Character parameters type, name, description, life, and dexterity
                char_type = Character.edit_char_type(self=1)
                print("Name")
                name = IO.input_str_choice(max_name_len)
                print("Description")
                desc = IO.input_str_choice(max_desc_len)
                print("Life")
                life = IO.input_integer_choice(max_stat)
                print("Dexterity")
                dex = IO.input_integer_choice(max_stat)
                # Create Character and append to list of character objects
                list_character_objects.append(Character(char_type, name, desc, life, dex))
            # Edit an existing object with the class Character
            elif sub_menu_choice == 3:
                print("Enter name of character you'd like to edit: ")
                name = IO.input_str_choice(max_name_len)
                # Function to check that name is in inventory and return index number in list
                in_inventory, char_index = Character.char_in_inventory(name)
                if in_inventory:
                    while True:
                        # User selects which character attributes to edit and then exits
                        print("1. Name, 2. Description, 3. Life, 4. Dexterity, 5. Exit")
                        edit_choice = IO.input_integer_choice(5)
                        if edit_choice == 1:
                            print("Enter new name")
                            list_character_objects[char_index].name = IO.input_str_choice(max_name_len)
                        elif edit_choice == 2:
                            print("Enter new description")
                            list_character_objects[char_index].desc = IO.input_str_choice(max_desc_len)
                        elif edit_choice == 3:
                            print("Enter new life")
                            list_character_objects[char_index].life = IO.input_integer_choice(max_stat)
                        elif edit_choice == 4:
                            print("Enter new dexterity")
                            list_character_objects[char_index].dex = IO.input_integer_choice(max_stat)
                        else:
                            break
                else:
                    print("Character not found in inventory.")
            # Remove an object with the class Character from the inventory list
            elif sub_menu_choice == 4:
                print("Which character would you like to remove?")
                name = IO.input_str_choice(max_name_len)
                in_inventory, char_index = Character.char_in_inventory(name)
                if in_inventory:
                    list_character_objects.pop(char_index)
                    print(name.capitalize() + "removed from inventory.")
                else:
                    print("Character not found.")
            # Exit to main menu
            else:
                break
    elif main_menu_choice == 2:
        while True:
            # User loops through the Item menu until they exit to the main menu
            IO.sub_menu(main_menu_choice)
            # Input integer choice function to ensure user enters valid menu choice
            sub_menu_choice = IO.input_integer_choice(max_sub_choice)
            # Print all Item objects in the list of items
            # Convert from strings to formatted tables in next release
            if sub_menu_choice == 1:
                if len(list_item_objects) == 0:
                    print("Your item list is empty")
                else:
                    Item.print_item_list(self=1)
            # Create object class Item and append to item list
            elif sub_menu_choice == 2:
                item_type = Item.enter_item_type(self=1)
                print("Name")
                name = IO.input_str_choice(max_name_len)
                print("Description")
                desc = IO.input_str_choice(max_desc_len)
                print("Attack")
                attack = IO.input_integer_choice(max_stat)
                print("Defend")
                defend = IO.input_integer_choice(max_stat)
                print("Heal")
                heal = IO.input_integer_choice(max_stat)
                print("Value")
                value = IO.input_integer_choice(max_stat)
                list_item_objects.append(Item(item_type, name, desc, attack, defend, heal, value))
            elif sub_menu_choice == 3:
                print("Enter the name of the item you'd like to edit.")
                name = IO.input_str_choice(max_name_len)
                # Function to check that item is in inventory and return index
                in_inventory, item_index = Item.item_in_inventory(name)
                if in_inventory:
                    while True:
                        print("1. Name, 2. Description, 3. Attack, 4. Defend, 5. Heal, 6. Value, 7. Exit")
                        edit_choice = IO.input_integer_choice(7)
                        if edit_choice == 1:
                            print("Enter new name")
                            list_item_objects[item_index].name = IO.input_str_choice(max_name_len)
                        elif edit_choice == 2:
                            print("Enter new description")
                            list_item_objects[item_index].name = IO.input_str_choice(max_desc_len)
                        elif edit_choice == 3:
                            print("Enter new Attack")
                            list_item_objects[item_index].attack = IO.input_integer_choice(max_stat)
                        elif edit_choice == 4:
                            print("Enter new Defend")
                            list_item_objects[item_index].defend = IO.input_integer_choice(max_stat)
                        elif edit_choice == 5:
                            print("Enter new Heal")
                            list_item_objects[item_index].heal = IO.input_integer_choice(max_stat)
                        elif edit_choice == 6:
                            list_item_objects[item_index].value = IO.input_integer_choice(max_stat)
                        else:
                            break
                else:
                    print("Item not found in inventory.")
            elif sub_menu_choice == 4:
                print("Which item would you like to remove?")
                name = IO.input_str_choice(max_name_len)
                in_inventory, item_index = Item.item_in_inventory(name)
                if in_inventory:
                    list_item_objects.pop(item_index)
                    print(name.capitalize() + "removed from inventory.")
                else:
                    print("Item not found in inventory.")
            else:
                break
    elif main_menu_choice == 3:
        # Save updated lists of character and item objects to pickle file my_hero_objects
        try:
            f = open("my_hero_objects.dat", "wb")
            pickle.dump(list_character_objects, f)
            pickle.dump(list_item_objects, f)
            f.close()
            print("Character and item inventories saved")
        except:
            print("Error, inventories not saved.")
    elif main_menu_choice == 4:
        # Break while loop to exit program
        print("Goodbye.")
        break
    else:
        # The IO function input integer choice should prevent this from ever happening, but users are creative
        IO.main_menu()