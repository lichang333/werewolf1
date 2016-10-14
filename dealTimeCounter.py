#coding:utf-8
import api
import database

def dealTimeCounter():
    print 'dTC ok'
    if database.fail > 0:
        database.fail -= 1
        if database.fail == 30:
            print 'Time up'
            api.sendMessage(u'30s过去了，我说没人吧',database.chatId);
        if database.fail == 1:
            print 'Time up'
            api.sendMessage(u'60s过去了，我说没人吧',database.chatId);
