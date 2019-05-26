from os import listdir
from os.path import isfile, join
import sys
import io

mypath = 'output'
outfile = 'out.txt'

if len(sys.argv) >= 3:
    mypath = sys.argv[1]
    outfile = sys.argv[2]

onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    with io.open(f, 'r', encoding='utf-8') as ifile:
        with io.open(outfile, 'a', encoding='utf-8') as ofile:
            for line in ifile:
                ofile.write(line)
print('Merging Done')