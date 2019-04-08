'''
Example of a user defined class and objects
'''

class Person:
    # functions of a class must have at least one parameter
    # and the first parameter is generally defined as 'self'
    # 'self' is not a keyword; it's just another variable.
    # The parameter 'self' is nothing but the invoking object
    # For example, if p1.info() is called, self = p1
    def info(self):
        print('Name = ', self.name)
        print('City = ', self.city)
        print('Email = ', self.email)
        print('-'*50)

# end of class Person

def main():
    # classname along with () is an instruction to Python to create
    # a new object of that class, and return a reference of the same
    p1 = Person()
    # So, p1 now has the reference of the newly constructed object
    # in the heap. If p1 is assigned with something else, the object
    # that it currently refers to becomes garbage, and will recollected
    # by Python at some point in time in the future.
    p1.name = 'Vinod'
    p1.email = 'vinod@vinod.co'
    p1.city = 'Bangalore'

    p1.info()

    p2 = Person()
    p2.name = 'John'
    p2.email = 'john@example.com'
    p2.city = 'Dallas'
    p2.info()

if __name__=='__main__': main()