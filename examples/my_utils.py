'''
Some useful utility functions.
'''
import json
import datetime
from calendar import monthrange
import sys

class Calendar:
    def __init__(self, month=None, year=None):
        if month is None:
            # call to the @month.setter
            self.month = datetime.date.today().month
        else:
            self.month = month

        if year is None:
            # call to the @year.setter property
            self.year = datetime.date.today().year
        else:
            self.year = year
        
    @property
    def month(self): return self.__month

    @month.setter
    def month(self, value):
        if type(value) != int: raise TypeError('Only int is allowed for month')
        if value<1 or value>12: raise ValueError('Month should be between 1 and 12')
        self.__month = value
        
    @property
    def year(self): return self.__year

    @year.setter
    def year(self, value):
        if type(value) != int: raise TypeError('Only int is allowed for year')
        if value<1970: raise ValueError('Year should be more than 1970')
        self.__year = value

    def show(self):
        month_name = datetime.date(self.__year, self.__month, 1).strftime('%B')
        print('Calendar for %s, %s' % (month_name, self.__year))

        # from calendar import monthrange
        # monthrange(year, month) returns a tuple with 2 numbers
        # first --> 0-6 (mon-sun) of 1st day of the month
        # second --> last day in the given month/year combination
        mr = monthrange(self.__year, self.__month)
        offset = mr[0] + 1
        max_days = mr[1]
        print('Su Mo Tu We Th Fr Sa ')
        print('-' * 21)

        # don't print balnk spaces for month starting on a sunday
        # for example, January 2017
        if offset !=7: print('   '*offset, end='')

        for i in range(1, max_days+1):
            print('%2d ' % (i), end='')
            if (i+offset)%7 == 0: print()

        print()


def dirr(obj):
    return [attr for attr in dir(obj) if attr[:1] != '_']

def csv2json(filename):
    list_of_people = []
    with open(filename) as file:
        header = file.readline().strip().split(',')
        for line in file:
            data = line.strip().split(',')
            p1 = dict(zip(header, data))
            list_of_people.append(p1)

    # file is automatically closed here
    dot_index = filename.index('.')
    new_filename = filename[:dot_index] + '.json'
    
    with open(new_filename, 'w') as file:
        json.dump(list_of_people, file, indent=3)

def csv2json_v2(filename):
    with open(filename) as file:
        header = file.readline().strip().split(',')
        list_of_people = [
            dict(zip(header, line.strip().split(',')))
            for line in file
        ]
        
    dot_index = filename.index('.')
    new_filename = filename[:dot_index] + '.json'
    
    with open(new_filename, 'w') as new_file:
        json.dump(list_of_people, new_file, indent=3)


def json2csv(filename):
    with open(filename) as file:
        data = json.load(file)
        header = ','.join(data[0].keys()) + '\n'
        rows = [
            ','.join(d.values()) + '\n'
            for d in data
        ]
        rows.insert(0, header)
        with open('output.csv', 'w') as outfile: outfile.writelines(rows)


def main():
    try:
        c1 = Calendar()
        if len(sys.argv) > 1:
            # call to the @month.setter property
            c1.month = int(sys.argv[1])  # second parameter
        if len(sys.argv) > 2:
            c1.year = int(sys.argv[2])  # third parameter
        
        c1.show()
    except Exception as err:
        print('There was an error:', err)


if __name__=='__main__': main()