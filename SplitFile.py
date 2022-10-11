'''Split a given input file into files of size `size`'''

import os
import sys

def split_file(filename, size=None):
    '''Split a file into files of size `size`'''
    if not size:
        size = 1024*1024*8
    with open(filename, 'rb') as f:
        fileno = 1
        while True:
            chunk = f.read(size)
            if not chunk:
                break
            if not os.path.exists(f'{filename}split'):
                os.mkdir(f'{filename}split')
            with open(f'{filename}split\\{filename}{fileno:08d}.part', 'wb') as f2:
                f2.write(chunk)
            fileno += 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} filename [size: default 8MB]')
        sys.exit(1)
    if len(sys.argv) == 2:
        size = None
    else:
        size = int(sys.argv[2])
    split_file(sys.argv[1], size)