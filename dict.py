#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from DictionaryServices import *
import re


def main():
    try:
        searchword = sys.argv[1].decode('utf-8')
    except IndexError:
        errmsg = 'You did not enter any terms to look up in the Dictionary.'
        print errmsg
        sys.exit()
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        errmsg = "'{0}' not found in Dictinary.".format(searchword)
        print errmsg.encode('utf-8')
    else:
        print fmt(dictresult.encode('utf-8'))


def fmt(str_raw_results):
    fmt_str = '\n' + str_raw_results + '\n'
    fmt_str = re.sub(r'(▶\w*)', r'\n\n\1\n', fmt_str)
    fmt_str = re.sub(r' (\d+) ', r'\n\n(\1) ', fmt_str)
    fmt_str = re.sub(r' (•) ', r'\n\1 ', fmt_str)
    fmt_str = re.sub(r' *(ORIGIN) ', r'\n\n\1\n', fmt_str)
    fmt_str = re.sub(r' *(PHRASES) ', r'\n\n\1\n', fmt_str)
    return fmt_str


if __name__ == '__main__':
    main()
