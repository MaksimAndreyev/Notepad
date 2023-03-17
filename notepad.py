from json import *
from datetime import datetime


def read_text():
    f = open('data.json', 'r')
    a = f.readlines()
    f.close()
    return a


def info():
    print('Type "write" to create a new note')
    print('Type "read" to view existing notes')
    print('Type "edit" to change existing note by its id')
    print('Type "delete" to delete a note by its id')
    print('Type "stop" to end working')


def read():
    f = open('data.json', 'r')
    headline = input('Write the headline of the note you want to view (to see all type "all"): ')
    for i in f:
        h = list(i.split())[1]
        if headline == 'all' or headline == h:
            print(i.strip('\n'))
    f.close()


def write():
    f = open('data.json', 'a')
    identity = str(hash(datetime.now()))[-4:]
    headline = input('Type the headline: ')
    text = input('Type the text: ')
    tm = str(datetime.now())[:-7]
    data = f'{identity} {headline} {text} {tm} \n'
    f.write(data)
    f.close()



def edit():
    identity = input('Type the id of the note you want to edit: ')
    a = read_text()
    new_text = input('Type new text: ')
    f = open('data.json', 'w')
    for i in a:
        if i[:4] != identity:
            f.write(i)
        else:
            s = list(i.split())
            s[2] = new_text
            f.write(' '.join(s))
    f.close()


def delete():
    identity = input('Type the id of the note you want to delete: ')
    a = read_text()
    f = open('data.json', 'w')
    for i in a:
        if i[:4] != identity:
            f.write(i)
    f.close()


while True:
    command = input('Type a command (for the list of commands type "info"): ').lower()
    if command == 'stop':
        break
    elif command in ('read', 'write', 'delete', 'info', 'edit'):
        exec(command+'()')
    else:
        print('Wrong command')
