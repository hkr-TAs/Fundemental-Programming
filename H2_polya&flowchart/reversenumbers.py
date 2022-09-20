"""Bob has a list of binary numbers and he needs help reversing them all. Bob would like to have it printed on the screen."""

sample_number = ["10101010", "01011011", "10101000", "01001101", "10101110"]


## Solution with for loop
for number in sample_number:
    print(number[::-1])


## Solution with while loop
count = 0
while count != len(sample_number):
    reversed_binary = sample_number[count][::-1]
    print(reversed_binary)
    count += 1