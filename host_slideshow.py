#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import os
from IPython.nbconvert.postprocessors import serve

def main():
    try:
        fname_slideshow = sys.argv[1].decode('utf-8')
    except IndexError:
        errmsg = 'You did not enter slideshow file.'
        print errmsg
        sys.exit()
    serve.main(fname_slideshow)

    




if __name__ == '__main__':
    main()
