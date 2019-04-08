'''
find the sum of all numbers in the input file
'''

def main():
    valid_inputs = []
    invalid_inputs = []
    with open('numbers.data') as file:
        for line in file:
            # skip if the line does not contain anything
            # if line.strip()=='': continue

            try:
                num = float(line)
                valid_inputs.append(num)
            except ValueError:
                invalid_inputs.append(line.strip())
    
    total = sum(valid_inputs)
    print('Valid numbers =', valid_inputs)
    print('Total of numeric values =', total)
    print('Invalid inputs', invalid_inputs)

if __name__=='__main__': main()