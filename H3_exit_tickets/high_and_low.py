"""
In this little assignment you are given a string of numbers separated by spaces, 
and have to return the highest and lowest number. The function should be named 'high_and_low' and 
is to be called from the main() method


Examples

high_and_low("1 2 3 4 5") -> return "5 1"
high_and_low("1 2 -3 4 5") -> return "5 -3"
high_and_low("1 9 3 4 -5") -> return "9 -5"

Notes

  -  There must always be at least one number in the input string.
  -  Return string must be two numbers separated by a single space, and highest number is first.

"""

def high_and_low(numbers: str) -> str:
    max_num = 0
    min_num = 0
    for number in numbers.split():
        number = int(number)
        if number > max_num:
            max_num = number
        elif number < min_num:
            min_num = number
    return f'{max_num} {min_num}'


def main() -> None:
    print(high_and_low("1 4 5 -2 -3 99"))


if __name__ == "__main__":
    main()