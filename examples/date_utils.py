'''
This is a utility module for helping with date operations.

Version 1.0
By Vinod <vinod@vinod.co>
'''

# data members of this module (prefix them with double underscores
# if you want them to be module level (private))
author = 'Vinod'
email = 'vinod@vinod.co'

# use the 'def' keyword to define a function
def max_days_in_month(month):
    '''
    This function accepts an int as parameter representing the month number
    starting from 1 (for Jan) till 12 (for Dec), and returns an int representing
    the number of days in the given month.

    In case if the argument is not an int, a TypeError is raised.
    '''

    if type(month) != int:
        raise TypeError('Only int is accepted as month.')
    
    if month<1 or month>12: raise ValueError('Only 1 to 12 are expected as month')

    if month == 2: return 28
    elif month in [4, 6, 9, 11]: return 30
    else: return 31
# ------ end of max_days_in_month function

if __name__=='__main__':
    md = max_days_in_month(4)
    print('max days in april is', md)

# print('name of this module (date_utils) is', __name__)
# __name__ is equals to '__main__' if this module is run directly; but is 'date_utils' if imported in another module.