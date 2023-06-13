import os

def pathJoin(pathArray):
    return os.path.join(pathArray)

def changeCurrentDir(path):
    print('The current directory '+ os.getcwd()+' will change to '+path)
    os.chdir(path)
    print('And current directory is : '+ os.getcwd())