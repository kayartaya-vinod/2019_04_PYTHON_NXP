class Employee:
    '''
    Class Employee by Vinod
    '''
    def __init__(self, name=None, email=None, salary=None):
        '''
        When Employee() is called, Python creates a new object (empty),
        and then calls the __init__ function by supplying the reference
        of the newly constructed object
        '''
        self.__name = name
        
        if type(salary) in (int, float) and salary>=20000:
            self.__salary = salary
        else:
            self.__salary = 20000

        self.__email = email
        # prefixing a member variable with __ hides it from outside access.
        # For example, e1.__salary = -50000 will not affect the hidden
        # member variable __salary. These however can be accessed from
        # any member function of this class (like display_details).

    def __str__(self):
        '''
        Define this function to textually represent an object.
        For example, print(e1)
        '''
        return 'Name={}, Salary=Rs.{}'.format(self.__name, self.__salary)

    def display_details(self):
        '''
        The parameter "self" represents the invoking object.
        For example, if this method was called as e1.display_details(),
        then self == e1
        '''
        print('Name     = %s' % self.__name)
        print('Salary   = %s' % self.__salary)
        print('Email    = %s' % self.__email)
        print('-'*25)

# end of class Employee

def main():
    e1 = Employee('Ramesh', 'ramesh@xmpl.com')
    e1.display_details()

    e2 = Employee('Harish')
    e2.__salary = 'asdf' # this is outside access
    e2.display_details()

if __name__=='__main__': main()
