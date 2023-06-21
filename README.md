# My Hero Edit Object Inventory
The edit game objects program was created to demonstrate the coding skills learned in my Foundations of Programming - Python class.  The program allows users to add, edit, and remove objects from the Classes Character and Item for use in the My Hero game and uses try/except and if/else trees to ensure that the user enters valid field values.

# Classes and Objects
The advantage of object oriented programming (OOP) over the lists, tuples, and dictionaries used in early modules is that the the programmer doesn't have to remember the index/position of an object attribute, the attribute is called by name. The class Character has five attributes (Figure 1).  If I managed my characters as a list of list I would have to remember that 0 = character type, 1 = name, 2 = description, etc.  Instead, I just need to find the character in the list and then I can call attributes by name.  

![Constructor for class Character](https://github.com/AFolmer/MyHero/assets/132308533/c30ba178-d0e4-487e-91ea-a70735ae9903)
### Figure 1: Constructor for class Character

The other advantage of OOP is that I can document the constructor function __init__ so that PyCharm displays class information as a popup when I scroll over Character instead of making the programmer scroll up and down the page (Figure 2).  The documentation goes between three sets of quotation marks, """ """, and includes the following:
 - :param (input name): the function inputs/parameters names and descriptions
 - :return (output name): the function outputs/returns names and descriptions
I also used the python function __repr__ to define the text string used to identify each object.  

![PyCharm pop up with Character attributes](https://github.com/AFolmer/MyHero/assets/132308533/a6a9af56-798c-45e2-b433-1d791171f205)
### Figure 2: PyCharm pop up with Character attribute information

