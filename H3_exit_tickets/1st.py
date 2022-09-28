# Previous knowledge of if-statements, loops, FUNCTIONS, flowcharts and polyas problem solving techniques.
"""
Ca half a page about what you have learned. 
Even if you solved 3 of the assignments the report should be half a page long.
https://hkr.instructure.com/courses/5190/assignments/56399 <- lets look at the assignment description together.
"""

"""
We have also started looking at your labs that you have sent in and left some comments on some of you. Any questions?
Again, please do not share your code or the comments you have got with your friend before the deadline!!!
"""

# Examples with f strings

s1 = "a"
s2 = "ab"
s3 = "abc"
s4 = "abcd"

print("_" * 10)  # Just to show that we have 10 spots

# Align to right
print(f"{s1:>10}")
print(f"{s2:>10}")
print(f"{s3:>10}")
print(f"{s4:>10}")

# Align to left
print(f"{s4:<10}")

# Align to center
print(f"{s4:^10}")

print(f"{s4:^10} + {s4:>10}!")


print("_" * 23)
print(f"{s4:^10} + {s4:>10}!")

# Exercises with functions
def my_function(name):
    print("Your name is ", name, ". You are very very welcome")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function2(fname, lname):
    print(fname + " " + lname)


# BAD
my_function2("Emil")
# GOOD
my_function2("Emil", "Svensson")

# Typing in python
def foo(x: int) -> int:
    x = x * 2
    return x


# return, pass
