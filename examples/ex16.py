'''
ex16.py
limit the depth of traversing in os.walk()
'''
import os

def main():
    initial_path = '/Users/vinodkumar/Desktop'
    depth_to_traverse = 1
    initial_depth = initial_path.count(os.sep)

    for (root, dirs, files) in os.walk(initial_path):
        if root.count(os.sep)>= initial_depth + depth_to_traverse:
            dirs.clear() # mutate the dirs, so that no further traverse
        print('root=', root, 'dirs=', len(dirs), 'files=', len(files))

if __name__=='__main__': main()