"""Bob has a list of binary binarys and he needs help reversing them all. Bob would like to have it printed on the screen."""

binary_numbers = ["10101010", "01011011", "10101000", "01001101", "10101110"]


## Solution with for loop
for binary in binary_numbers:
    print(binary[::-1])

# for number in sample_number:
#     test_number = 0
#     number = int(number)
#     while number > 0:
#         remainder_number = number % 10
#         test_number = (test_number * 10) + remainder_number
#         number = number // 10
#     print("Value after reverse : {}".format(test_number))


## Solution with while loop
count = 0
while count != len(binary_numbers):
    reversed_binary = binary_numbers[count][::-1]
    print(reversed_binary)
    count += 1
