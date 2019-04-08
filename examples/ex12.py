class Employee:
    '''
    Class Employee by Vinod
    '''
    def __init__(self, name=None, email=None, salary=20000):
        '''
        When Employee() is called, Python creates a new object (empty),
        and then calls the __init__ function by supplying the reference
        of the newly constructed object
        '''
        self.__name = name

        # if type(salary) in (int, float) and salary>=20000:
        #     self.__salary = salary
        # else:
        #     self.__salary = 20000
        self.salary = salary  # pass the control to the setter

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

    # the following function is going to be a property (getter/accessor).
    # The properties are defined like functions but used like variables.
    # For example, following property is used like below:
    # e1 = Employee('James', 'james@xmpl.com', 25000)
    # print('e1 salary is ', e1.salary)
    @property
    def salary(self):
        return self.__salary

    # in constructor, instead of validation:
    # self.salary = salary

    @salary.setter
    def salary(self, value):
        if type(value) in (int, float) and value>=20000:
            self.__salary = value
        else:
            raise Exception('Salary must be a number >= 20000')

    def __iadd__(self, value):
        if type(value) is str:
            self.__name += value
        elif type(value) in (int, float):
            self.salary += value # calls the @salary.setter function
        else:
            raise TypeError('Invalid type for RHS; only str,int,float allowed')
        return self

    def __add__(self, value):
        if type(value) is Employee:
            return self.salary + value.salary
        elif type(value) in (int, float):
            return self.salary + value
        else:
            raise TypeError('Incomatible type for + operation')

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
    e1 = Employee('Ramesh')
    e2 = Employee('Rajesh', None, 25000)
    e3 = Employee('Mahesh', None, 45000)
    total = e1 + (e2 + e3)
    print('total', total)

def _main():
    e1 = Employee('Ramesh', 'ramesh@xmpl.com', 25000)
    print('Ramesh\'s salary is', e1.salary) # @property salary called
    e1.salary = 50000 # @salary.setter called

    # + __add__
    # - __sub__
    # * __mul__
    # / __div__
    # += __iadd__
    # -+ __isub__

    e1 += ' Kumar'  # should be appended to name
    e1 += 5000      # shound be added to salary

    e1.display_details()

    # inside constructor, instead of validation:
    # self.salary = salary

    e2 = Employee('Harish')
    e2.__salary = 55000 # this is outside access; does not affect the
    #  internal __salary variable in the Employee object.
    
    e2.display_details()

if __name__=='__main__': main()
