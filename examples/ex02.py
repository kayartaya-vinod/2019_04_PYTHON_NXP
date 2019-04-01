# A script to accept two numbers and 
# print sum, difference, product and quotient 

n1 = input('Enter a number: ')
n2 = input('Enter another number: ')

n1 = int(n1)
n2 = int(n2)

total = n1 + n2
diff = n1 - n2
product = n1 * n2
quotient = n1 // n2  # single slash --> flaot divition, double slash --> int division
remainder = n1 % n2

print('''Total = %s
Diff = %s
Product = %s
Quotient = %s
Remainder = %s''' % (total, diff, product, quotient, remainder))

