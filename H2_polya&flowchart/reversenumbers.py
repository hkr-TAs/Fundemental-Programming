sample_number = int(input("Number to be reversed: "))
test_number = 0
while sample_number > 0:
    remainder_number = sample_number % 10
    test_number = (test_number * 10) + remainder_number
    sample_number = sample_number // 10
print("Value after reverse : {}".format(test_number))