"""Bob has a list of binary numbers and he needs help reversing them all. Bob would like to have it printed on the screen."""

sample_number = ["10101010", "01011011", "10101000", "01001101", "10101110"]

<<<<<<< HEAD
# Short solution
for number in sample_number:
    print(number[::-1])

# for number in sample_number:
#     test_number = 0
#     number = int(number)
#     while number > 0:
#         remainder_number = number % 10
#         test_number = (test_number * 10) + remainder_number
#         number = number // 10
#     print("Value after reverse : {}".format(test_number))

=======

## Solution with for loop
for number in sample_number:
    print(number[::-1])

>>>>>>> b8dd73942c21d78b8610c3a8be82f0e486be074e

## Solution with while loop
count = 0
while count != len(sample_number):
    reversed_binary = sample_number[count][::-1]
    print(reversed_binary)
<<<<<<< HEAD
    count += 1
=======
    count += 1
>>>>>>> b8dd73942c21d78b8610c3a8be82f0e486be074e
