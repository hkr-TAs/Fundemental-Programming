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


## SOLUTION
def high_and_low(numbers: str) -> str:
    numbers = [int(i) for i in numbers.split()]
    return f"{max(numbers)} {min(numbers)}"


def main() -> None:
    assert high_and_low("1 4 5 -2 -3 99") == "99 -3"


if __name__ == "__main__":
    main()
