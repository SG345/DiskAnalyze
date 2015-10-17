import os
DIRPATH = os.path.expanduser('~')

for root, directories, filenames in os.walk(DIRPATH):
    for filename in filenames:
        currentfile = os.path.join(root,filename)
        currentstat = os.stat(currentfile)
        currentsize = currentstat.st_size
        result = [filename, currentsize]
        print result