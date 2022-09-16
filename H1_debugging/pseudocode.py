"""
Here's some pseudocode you will have to translate to python code

ask the user their name
if their name is Sandra
then write no access
if their name is Adis
then write error
else print the name and greet them welcome

"""


name = input("Whats your name? ")
if name == "Sandra":
    print("no access")
elif name == "Adis":
    print("error")
else:
    print(f"Welcome {name}")
