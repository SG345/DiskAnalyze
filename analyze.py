import os
import sys
import json
import operator


DIRPATH = os.path.expanduser('~')
DIRPATH = os.path.join(DIRPATH, 'DiskAnalyze')

files = []

print 'Scanning through your disk. Please wait...'
print 'The process may take up to 20 minutes...'

result = ()
json_str=""
for root, directories, filenames in os.walk(DIRPATH):
    for filename in filenames:
        currentfile = os.path.join(root,filename)
        currentstat = os.stat(currentfile)
        currentsize = currentstat.st_size
        #tup = (filename, currentsize)
        tup = (currentsize, filename)
        files.append(tup)

files.sort(cmp=None,key=None,reverse=True) #Sort files in non-increasing order according to their respective file size

for f in files:
    print f