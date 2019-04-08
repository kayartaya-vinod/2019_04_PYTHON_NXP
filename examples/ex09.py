'''
Exceptions Demo
'''

def main():
    n1 = input('Enter a number: ')
    n2 = input('Enter another number: ')

    try:
        n1 = int(n1)
        n2 = int(n2)
        n3 = n1 // n2
        print('{} / {} = {}'.format(n1, n2, n3))
        # print('%s / %s = %s' % (n1, n2, n3))
        # print(n1, '/', n2, '=', n3)
    except ValueError as err:
        print('Invalid value supplied')
        print('Root cause =', err)
    except ZeroDivisionError:
        print('Cannot divide by zero!')
    except Exception:  # fail safe block
        print('There was a problem!') 

if __name__=='__main__': main()
