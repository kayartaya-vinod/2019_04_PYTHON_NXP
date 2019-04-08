'''
ex15.py
Example for pathlib.Path
'''

from pathlib import Path
import sys

def print_dir_details(file_dir_name, n=0):
    p = Path(file_dir_name)
    print(' '*n, '-', p.name)
    if p.is_dir():
        n += 3
        for x in p.iterdir():
            print_dir_details(x.absolute(), n)
        n -= 3

def main():
    file_dir_name = '.'
    if len(sys.argv)>1: file_dir_name = sys.argv[1]

    print_dir_details(file_dir_name)

if __name__=='__main__': main()