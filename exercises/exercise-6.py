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


month = input('Enter the month of the year (Jan - Dec): ')
while True:
    try:
        day = int(input('Enter the day of the month: '))
        if day < 1 or day > 31:
            raise ValueError
        break
    except ValueError:
        print("Invalid day. The number must be in the range of 1-31.")

if month in ('Dec', 'Jan', 'Feb'):
    season = 'Fall' if month == 'Dec' and day < 21 else 'Winter'
elif month in ('Mar', 'Apr', 'May'):
    season = 'Winter' if month == 'Mar' and day < 20 else 'Spring'
elif month in ('Jun', 'Jul', 'Aug'):
    season = 'Spring' if month == 'Jun' and day < 21 else 'Summer'
else:
    season = 'Summer' if month == 'Sep' and day < 22 else 'Fall'

print(f'{month} {day} is in {season}')
