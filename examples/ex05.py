# Example for reusing an existing module using the import statement

# __name__ is a builtin python shell variable, representing the name of the 
# module loaded

# import date_utils
from date_utils import max_days_in_month

def main():
    m = int(input('Enter a month number: '))
    md = max_days_in_month(m)

    print('Number of days in the month', m, 'is', md)

if __name__=='__main__': main()

