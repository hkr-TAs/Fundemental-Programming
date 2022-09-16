# Previous knowledge of if-statements, boolean
# repetition for words like declare, initialize, assignment
# lådtyperna i flowcharts

# Autosave vscode File-> Auto Save

# Comments in python
""" Multi
line
docstrings
"""

"""
Tips!
Helpful shortcuts in VSCode
Ctrl+S to save the file you are on if Auto-Save isnt on

Ctrl+C for copy and Ctrl+V for paste
<<<<<<< HEAD
=======
Ctrl+F to find a specific symbol or a word in the code. Click on downwards arrow to open the Find and Replace tool.
>>>>>>> 72f0bdb4ce379990f085f8c28b8b362b52004f95
Ctrl+K+C to comment out a whole block Ctrl+K+U to undo

Ctrl+F to find a specific symbol or a name in the code. Click on downwards arrow or press Ctrl+H to open the Find and Replace tool.

Use TAB to ->     <- tab in the code TAB+SHIFT to undo
Ctrl+Shift+Arrowkeys to select text (left to right to select one symbol at the time, up and down to select a whole line)
Alt+Arrowkeys to move a line you're currently on up or down in the code
"""

name = input("Input your name here: ")
print(f"Your name is {name}. \n")
print("\t Welcome to HKR")

# f strings \t and \n
name = input("Enter your name >> ")
age = int(input("Enter your age >> "))
programme = input("Enter your programme >> ")

print(f"Name:\t{name}\n")
if age == 20:
    print(f"Age:\t{age}\n")
else:
    print(f"Age:\t{age}\n")
print(f"Programme:\t{programme}")

print(f"Your name is {name}", "Have a nice day", sep=". ", end="!\n")
