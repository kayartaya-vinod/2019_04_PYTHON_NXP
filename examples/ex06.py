'''
This example demonstrates the use of "while" loop
'''

# the keyword "def" is used for creating a user defined function
def multiplication_table(num):
    i = 1
    while i <= 10:
        print("{} * {} --> {}".format(num, i, num*i))
        i += 1

def line(chr = '.'):
    print(chr * 50)

def factorial(num):
    f = 1
    while num>0:
        f = f * num   # f *= num
        num = num -1  # num -= 1
        # print('f = {}, num = {}'.format(f, num))
    return f


def main():
    num = int(input('Enter a number: '))
    # multiplication_table(num)
    
    fact = factorial(num)
    print('Factorial of %s is %s' % (num, fact))
    # print('Factorial of %s is %s' % (num, factorial(num)))

# print('in ex06.py, value of __name__ is', __name__)
if __name__=='__main__':
    main()
    line('*')