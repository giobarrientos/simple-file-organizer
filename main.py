import os
import shutil

path = input("enter Path:")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extention = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)