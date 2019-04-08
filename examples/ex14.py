'''
ex14.py
Example of os.walk
'''

import os

def main():
    dirname = '/Users/vinodkumar/Sites/vinod.co.v4/dist'
    for (root, dirs, files) in os.walk(dirname):
        print('Content of the directory:', root)
        print('directories: ')
        for d in dirs: print('\t%s' % d)
        print('files: ')
        for f in files: print('\t%s' % f)
        print('-'*50)

if __name__=='__main__': main()