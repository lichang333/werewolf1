#coding:utf-8
import urllib
import urllib2
import re
import sys
import time
import json


def work(comm,value):
    global weburl
    global token

    data = urllib.urlencode(value)
    baseurl = weburl + token
    fail = 1
    times = 1
    while fail and times < 3:
        try:
            req = urllib2.Request(baseurl+comm,data)
            res = urllib2.urlopen(req)
            #print res.read()
            return_data = json.loads( res.read() )
        except:
            print '--------',comm,'fail, time',times
            print sys.exc_info()
            time.sleep(1)
            times += 1
            if times == 3:
                return_data = {}
        else:
            fail = 0

    if return_data.has_key('ok'):
        if return_data['ok'] == True:
            if comm == '/getupdates':
                if len(return_data['result']):
                    global update_id
                    result = return_data['result'][-1]
                    update_id = result['update_id'] + 1

    return return_data

def sendMessage(text,send_to):
    #print text,send_to
    
    value = {
            'chat_id':send_to,
            'text' : unicode(text).encode('utf-8'),
            }
    return work('/sendmessage',value)
    


weburl = 'https://api.telegram.org/bot'
token_file = open('token.secret','r')
token = token_file.readline()
token = token.strip()
token_file.close()
update_id = 0
