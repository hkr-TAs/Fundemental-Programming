"""
Here you will create a function that accepts a string and calculates the number of upper case letters and 
lower case letters in the inputted string. The function should be called 'upper_and_lower' and is to be called from the main() method.

Examples

upper_and_lower("The Quick Brown Fox") -> return 4, 12
upper_and_lower("The Sun Is Shining") -> return 4, 11

Notes
  
  - Return value of the function should be two integers
  - There should also be a print statement in the **main()** method printing the 'highest' and 'lowest' results 
    returned from the function.
"""

def upper_and_lower(sentence: str) -> tuple:
    return sum(1 for letter in sentence if letter.isupper()), sum(1 for letter in sentence if letter.islower())

def main() -> None:
    test_one = upper_and_lower("The Quick Brown Fox")
    test_two = upper_and_lower("The Sun Is Shining")
    assert test_one == (4, 12)
    assert test_two == (4, 11)

if __name__ == '__main__':
    main()