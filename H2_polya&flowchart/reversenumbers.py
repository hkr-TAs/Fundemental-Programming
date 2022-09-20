"""Bob has a list of binary binarys and he needs help reversing them all. Bob would like to have it printed on the screen."""

binary_numbers = ["10101010", "01011011", "10101000", "01001101", "10101110"]


## Solution with for loop
for binary in binary_numbers:
    print(binary[::-1])


## Solution with while loop
count = 0
while count != len(binary_numbers):
    reversed_binary = binary_numbers[count][::-1]
    print(reversed_binary)
    count += 1