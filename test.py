import os
reader = open("pathes.txt", 'r')
pathstr = reader.read()
print(pathstr)
print(os.path.isfile(pathstr))
