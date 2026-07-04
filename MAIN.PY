from pathlib import Path
import os

def readfileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}. {items}")


def createfile():
    try:
        readfileandfolder()
        name = input('please enter the file name')
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input('what you want to write in this file')
                fs.write(data)
            print('file created successfully')
        else:
            print('this file is already exist')

    except Exception as err:
        print('error is',err)

def readfile():
    try:
        readfileandfolder()
        name = input('please enter the file name')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print('file read successfully')
        else:
            print('this file is not exist')
    except Exception as err:
        print('error is',err)

def updatefile():
    try:
        readfileandfolder()
        name = input('please enter the file name you want to update')
        p= Path(name)
        if p.exists() and p.is_file():
            print('press 1 for changing the file name')
            print('press 2 to overwritethe file')
            print('press 3 to append the file')

        res = int(input('please tell your response'))
        if res == 1:
            newname = input('please enter the new name of the file')
            p2 =Path(newname)
            p.rename(p2)
        print('file name changed successfully')


        if res == 2:
            with open(p,'w') as fs:
                data = input('please enter the data to overwrite the file')
                fs.write(data)
            print('file overwritten successfully')
            
        if res == 3:
            with open(p,'a') as fs:
                data = input('please enter the data to append thw file')
                fs.write(' '+data)
            print('file appended successfully')
    except Exception as err:
        print('error is',err)  

def deletefile():
    try:
        readfileandfolder()
        name = input('please enter the file name you want to delete')
        p= Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print('file deleted successfully')
        else:
            print('this file is not exist')
    except Exception as err:
        print('error is',err)  

                  







print('press 1 for creating a new file')
print('press 2 for read the file')
print('press 3 for updating the file')
print('press 4 for deleting a file ')

check =int(input('please tell your choice'))

if check == 1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()