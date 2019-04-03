'''
More loop examples
'''
# FALSE = false = False
# TRUE = true = True
TRUE,FALSE = True,False

def is_prime(num):
    # try and divide num by all numbers from 2 till num/2
    limit = num//2
    i = 2
    while i <= limit:
        if num % i == 0: return False # takes the control outside the function
        i += 1
    return True

def main():
    num = int(input('Enter a number: '))
    if is_prime(num):
        print('%d is a prime number' % num)
    else:
        print('%d is a composite number' % num)

if __name__=='__main__': main()