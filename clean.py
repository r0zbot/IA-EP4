#!/usr/bin/env python3
# clean UTF
import glob
import sys
from ftfy import fix_encoding

filenames = sys.argv[1:]

for filename in filenames:
    print(filename)
    text =  open(filename,'r').read()
    f = open(filename.replace('.csv','_fixed.csv'),"a+")
    f.write(fix_encoding(text))
    f.close()