'''
More loop examples:
Accept two numbers and print all primes between them
'''

from ex07 import is_prime
from ex06 import line

def print_primes(start=1, end=100):
    while start <= end:
        if is_prime(start): print(start, end=', ')
        start += 1
    print()
    line()

# this function re-writes (overwrites/overrides) the above function definition
def print_primes(start=1, end=100):
    for n in range(start, end+1):
        if is_prime(n): print(n, end=', ')

    print()
    line('*')

def main():
    print_primes()
    print_primes(50)
    print_primes(end=50)
    print_primes(start=50)
    print_primes(200, 500)
    print_primes(end=200, start=50)

if __name__=='__main__':
    main()