'''
Demo of different types of function parameters
'''

def test1(a, b, c=100):
    '''
    a, b, and c are positional arguments.
    All of them are mandatory. By assigning values for parameters,
    they become optional.
    '''
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print()

# arbitrary arguments (variable length arguments)
def test2(*args):
    print('args is of type', type(args))
    print('args containt', args)
    print();

def total(*nums):
    print('total is', sum([n for n in nums if type(n) in (int, float)]))

# keyword arguments
def test3(**kwargs):
    print('kwargs is of type', type(kwargs))
    print('kwargs containt', kwargs)
    print()

def test4(a, b=10, *args, **kwargs):
    print('a =', a)
    print('b =', b)
    print('args =', args)
    print('kwargs =', kwargs)
    print() 

def main():
    test4(100)
    test4(10, 20, 30, 40)
    test4(30, 40, 50, 60, 70, x=10, y=20)

    # test3(name='vinod', email='vinod@vinod.co')
    # test3(a=10, b=20, c=30)
    # p1 = {'x': 10, 'y': 20}
    # test3(**p1) # individual key/value pairs are supplied as arguments

    # test1(10, 20, 30)
    # test1(a=10, c=12, b=300)
    # test1(22, 33)
    
    # test2(10, 20)
    # test2(123, 45, 603, 'vinod', False)

    # total(123, 34, 56, 'Vinod') # no.of args = 4
    # data = [10, 20, 'vinod', 49, False, 2.3]
    # total(*data) # no.of args is 6
    # total(data) # no.of args is 1

if __name__=='__main__': main()