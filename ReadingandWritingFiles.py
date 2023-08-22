import os

def pathJoin(pathArray):
    return os.path.join(pathArray)

def changeCurrentDir(path):
    print('The current directory '+ os.getcwd()+' will change to '+path)
    os.chdir(path)
    print('And current directory is : '+ os.getcwd())
def makeDir(path):
    #os.mkdir(path)
    os.makedirs(path)
def absolutePath(path):
    print(os.path.abspath(path))
def absolutePathCheck(path):
    return os.path.isabs(path)
def pathTypeCheck(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            print(path +' is a file')
        elif os.path.isdir(path):
            print(path+' is a directory')
    else:
        print(path + ' is not exist')