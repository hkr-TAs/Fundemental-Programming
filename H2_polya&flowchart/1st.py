# Previous knowledge of if-statements, loops, flowcharts and polyas problem solving techniques
# https://www.youtube.com/watch?v=zhL3EMFSm6o

# flowchart maker https://app.zenflowchart.com/app

# Polyas problem solving techniques are very important! (EXAM)


print(
    "1. Understand the problem (ignore the info that is not needed and pick out the important info)",
    "2. Create a plan (draw a picture, make a flowchart, write psudocode etc)",
    "3. Execute the plan",
    "4. Check if the result is correct",
)

# We can now make input validators that could be used on websites

z = 21
while z < 20:
    z = int(input("Enter number bigger than 20: "))
print("z is now under 20")


b = "20"
while b.isnumeric() == False:
    b = int(input("Enter a number: "))
print("We can now continue with a numeric value")
