# using if-elif-else and nested if-else construct
# Accept a month and print the number of days in it

mon = int(input('Enter a month (1-12): '))

if mon<1 or mon>12:
    print('Invalid month; must be between 1 and 12!')
else:
    if mon==2:
        print('It\'s february, and has 28 or 29 days')
    elif mon in [4, 6, 9, 11]:
        print('It has 30 days')
    else:
        print('It has 31 days')