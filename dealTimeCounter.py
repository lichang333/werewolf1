import api
import database

def dealTimeCounter():
    print 'dTC ok'
    print database.test
    database.example -= 1
    if database.example == 1:
        print 'Time up'
    
