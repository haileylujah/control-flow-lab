# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


month = input('Enter the month of the year (first three letters): ').upper()
# day = int(input('Enter the day of the month: '))
while True:
    try:
        day = int(input('Enter the day of the month: '))
        if day < 1 or day > 31:
            raise ValueError
        break
    except ValueError:
        print("Invalid day. The number must be in the range of 1-31.")

if month in 'DEC' and day > 20:
    print(f'{month} {day} is in Winter')
elif month in 'DEC' and day < 21:
    print(f'{month} {day} is in Fall')
elif month in ('JAN', 'FEB'):
    print(f'{month} {day} is in Winter')
elif month in 'MAR' and day > 19:
    print(f'{month} {day} is in Spring')
elif month in 'MAR' and day < 20:
    print(f'{month} {day} is in Winter')
elif month in ('APR', 'MAY'):
    print(f'{month} {day} is in Spring')
elif month in 'JUN' and day > 20:
    print(f'{month} {day} is in Summer')
elif month in 'JUN' and day < 21:
    print(f'{month} {day} is in Spring')
elif month in ('JUL', 'AUG'):
    print(f'{month} {day} is in Summer')
elif month in 'SEP' and day > 21:
    print(f'{month} {day} is in Fall')
elif month in 'SEP' and day < 22:
    print(f'{month} {day} is in Summer')
elif month in ('OCT', 'NOV'):
    print(f'{month} {day} is in Fall')
else:
    print("Please enter a correct month")