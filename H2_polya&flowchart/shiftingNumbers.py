"""
Bob was satisfied with your last job so he's asked you for another favor. 
    Bob would like to have each number in the list printed out, but with circular shift applied to it.
    He would also want to see a flowchart or a pseudocode of how its achieved in programming since he is also trying to learn it.
    
    An example of a binary number that has undergone a binary circular shift operation would look like this:

    10101010 -> 01010101

"""

binary_numbers = ["10101010", "01011011", "10101000", "01001101", "10101110"]

## Solutionwith for loop
print("\nSolution with for loop:\n")
for binary in binary_numbers:
    output = binary[1:] + binary[0]
    print(output)


## Solution with while
print("\nSolution with while loop\n")
index = 0
while index != len(binary_numbers):
    output = binary_numbers[index][1:] + binary_numbers[index][0]
    print(output)
    index += 1
