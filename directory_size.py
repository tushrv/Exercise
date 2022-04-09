import os, sys

try:
    directory = sys.argv[1] # get input as arguement from the user
except IndexError:
    sys.exit('No arguement given !!') 

directory_size = 0

all_size = {
             'Bytes':1,
             'Kilobytes': float(1)/1024,
             'Megabytes': float(1)/(1024*1024),
             'Gigabytes': float(1)/(1024*1024*1024)
            }

for (path,dirs,files) in os.walk(directory): # walk all directories ->  folders, subfolders, files.
    for file in files:
        filename = os.path.join(path,file)
        directory_size += os.path.getsize(filename) # get size of each file 

size_list = [str(round(all_size[key] * directory_size,2)) + ' ' + key for key in all_size] # list of all units

print('All units list : \n {}'.format(size_list))

if directory_size == 0:
    print('Directory empty')
else:
    for s in sorted(size_list)[::-1]: # smallest unit first
        print('Folder size: ' + s)