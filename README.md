# My Hero: Edit game objects program
The edit game objects program was created to demonstrate the coding skills learned in my Foundations of Programming - Python class.  The program allows users to add, edit, and remove objects with the Classes Character and Item and uses try/except and if/else trees to ensure that the user enters valid field values.  The objects are manged in the lists list_character_objects and list_item_objects and saved as a pickle file that can then be unpickled for use in the game My Hero.

# Classes and objects
Object oriented programming allows you to group the subjects in your program (e.g. retirement accounts, space ships, ice cream) into software objects.  These objects are created from a class: code that defines their attributes and methods.  
 - Class: the attributes and methods that define a group of objects
 - Attribute: the properties of an object in a class e.g. account balance, account owner, account type (Roth IRA, 401(k), UGTMA)
 - Methods: the behaviors of an object e.g. accept deposits, create account statement, add owner

One immediate advantage of object oriented programming (OOP) over the lists, tuples, and dictionaries used early in the class is that the the programmer doesn't have to remember the index/position of an object attribute, the attribute is called by a name. The class Character has five attributes (Figure 1).  If I managed my characters as a list of lists I would have to remember that 0 = character type, 1 = name, 2 = description, etc. and then update my code with new index numbers if I added or removed an attribute. With OOP, I can change my mind about attributes with minimal impact to the rest of the code.

![Constructor for class Character](https://github.com/AFolmer/MyHero/assets/132308533/c30ba178-d0e4-487e-91ea-a70735ae9903)

*Figure 1: Constructor for class Character*

Another advantage of OOP is that I can document the constructor function __init__ so that PyCharm displays class information as a popup when I scroll over the text Character instead of making the programmer scroll up and down the page (Figure 2).  The documentation goes between three sets of quotation marks, """ """, and includes the following:
 - :param (input name): the function inputs/parameters names and descriptions
 - :return (output name): the function outputs/returns names and descriptions
I also used the python function __repr__ to define the text string used to identify each object.  

![PyCharm pop up with Character attributes](https://github.com/AFolmer/MyHero/assets/132308533/a6a9af56-798c-45e2-b433-1d791171f205)

*Figure 2: PyCharm pop up with Character attribute information*

Finally, the biggest advantage in using classes and objects is the introduction of methods.  When using functions in python a variable cannot be changed within the function, it has to be passed in and out as a parameter/return.  When a function is created specific to a class it becomes a method and when an object is passed into that method all of the object attributes can be modified without listing them specifically. In the __init__ method I bring in the parameters for each object attribute, but I only need to return the object iteself (Figure 1).  The other methods used in this program are all @staticmethod, which means that they are associated with a class for documentation purposes, but don't directly change object attributes.  One of my goals for the next version of the program is to consolidate the functions and code blocks used to manipulate my objects and turn them into methods aligned to their class.

# Validating user entered data - try/except and if/else
The goal of this program is to create objects that can be used to support a game, which means that I need to define rules for object attributes and write code to ensure that users follow the rules.  Step 1 is to create constants used to enforce the rules (Figure 3).  I used constants at the program level rather than entering a specific min/max each time I call a function so that if I decide to change them (e.g. add a new menu choice, which changes the constant max_main_choice) I only have to make the change in one place.

![Constants defining variable parameters](https://github.com/AFolmer/MyHero/assets/132308533/8cec93f5-c402-4eb1-a6ca-e3eca37e5b2f)

*Figure 3: Constants used to enforce user input parameters

Next, I created two validation functions in the class IO (input/output).  The first function accepts user input and checks that the input is a number between a predefined minimum and maximum (Figure 4).  On lines 195 & 196 the function tries to save the input user_choice as an integer.  If the user enters text or a non-whole number (197) the function notifies the user that they need to enter an integer (198).  If there is any other kind of error (199) the function notifies the user that there was an unknown error.  This triggers a warning that bare except clauses are a bad idea, but users can be very creative in breaking things so I used it anyway.  If the function is able to execute the code in try, it moves on to else.  The next step in validating the integer is to use an if statement to check that the value is between my minimum and maximum and either accept the value, or else notify the user that they need to try again and enter a value in range.  On line 188 you can see that input_integer_choice is used 19 times within my program to validate menu choices and object attributes and on line 210 the function input_str_choice is used 12 times to validate strings and check for length.   

![Function to validate user input for an integer](https://github.com/AFolmer/MyHero/assets/132308533/5fbb2417-66d2-47e9-882e-5f8a796be0ec)

*Figure 4: Function to validate that user entered integer is a number between 0 and a maximum value*

# Pickle and unpickle
In the first few modules of my python class we used for loops to save and reimport our data as comma separated values (CSV) in text files.  This method results in a standalone data file, but it is really easy to make mistakes and takes too much processing power in larger programs. In this program I've moved on to a much simpler method: pickling. A pickle file takes complex data, such as lists and dictionaries, and saves it as a binary file.  The important thing to remmeber is to add the line 'import pickle' to your program to use pickle functionality, save the file as '.dat' for data, and always pickle and unpickle in the same order.  From there, use the pickle.load (Figure 5) and pickle.dump (Figure 6) functions to load and save files. 

![Unpickle character and item lists](https://github.com/AFolmer/MyHero/assets/132308533/23499877-727b-4cfa-a5dc-1f0629126265)

*Figure 5: Unpickle character and item lists

![Pickle character and item lists](https://github.com/AFolmer/MyHero/assets/132308533/ebbf3a2b-89d3-4e2f-9608-3b08be68690d)

*Figure 6: Pickle character and item lists

