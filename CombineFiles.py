'''Combines split files in directory `dirname` into single file `filename`'''

import os
import sys


def combine_files(dirname=None, delete=False, filename=None):
    '''Combine files in directory `dirname` into single file `filename`'''
    files = sorted([file for file in os.listdir(dirname) if file.endswith('.part')])
    if not filename:
        filename = files[0][:-13]
    with open(filename, 'wb') as f:
        for file in files:
            with open(os.path.join(dirname, file), 'rb') as f2:
                f.write(f2.read())
    if delete:
        for file in files:
            os.remove(os.path.join(dirname, file))


if __name__ == '__main__':
    if len(sys.argv) > 4:
        print(f'Usage: {sys.argv[0]} [DIRNAME: optional | default current directory] [DELETE: optional | default True] [FILENAME: optional]')
        sys.exit(1)
    # sys.argv.appends('D:/Music/Hentai Mode.mp3split')
    if len(sys.argv) == 1:
        dirname = os.getcwd()
        delete = True
        filename = None
    elif len(sys.argv) == 2:
        dirname = sys.argv[1]
        delete = True
        filename = None
    elif len(sys.argv) == 3:
        dirname, delete = sys.argv[1:-1]
        filename = None
    else:
        dirname, delete, filename = sys.argv[1:]
    combine_files(dirname, bool(delete), filename)
