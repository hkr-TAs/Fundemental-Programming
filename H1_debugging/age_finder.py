print("\nWelcome to age finder!\n")
print("The game will try and find your age range\n")

start_age = 20

over = input(f"Is your age over {start_age}? (y/n) >> ")

if 'over' == 'y' or over == 'Y':
   over = input(f'Is your age over {start_age+20}? (y/n)')
   if over == 'n' | 'over' == 'N':
       print(f'Your age range is between {start_age} and {start_age+20}')
   elif over == 'y' or 'over' == 'Y':
       print(f'You are over {start_age+20}')
elif 'over' == False or over == 'N':
   print('I give up!')
