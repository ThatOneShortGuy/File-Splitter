'''Combines split files in directory `dirname` into single file `filename`'''

import os
import sys

def combine_files(dirname, filename=None, delete=False):
    '''Combine files in directory `dirname` into single file `filename`'''
    if not filename:
        filename = dirname.replace('split', '')
    with open(filename, 'wb') as f:
        for filename in os.listdir(dirname):
            with open(os.path.join(dirname, filename), 'rb') as f2:
                f.write(f2.read())
    if delete:
        for filename in os.listdir(dirname):
            os.remove(os.path.join(dirname, filename))
        os.rmdir(dirname)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} dirname [filename: default dirname - split] [delete: default False]')
        sys.exit(1)
    if len(sys.argv) == 2:
        filename = None
        delete = False
    elif len(sys.argv) == 3:
        filename = sys.argv[2]
        delete = False
    else:
        filename = sys.argv[2]
        delete = bool(sys.argv[3])
    combine_files(sys.argv[1], filename, delete)