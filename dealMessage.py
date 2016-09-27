#coding:utf-8
import api
import database
import re

def F_text(text,send_by,chat):
    print text , chat['id']
    #api.sendMessage(text,chat['id'])

    if re.match(r'/chaosGame(@cdqzWerewolfBot)?',text):
        api.sendMessage(u'开始混乱模式',chat['id']);

    
    if re.match(r'/normalGame(@cdqzWerewolfBot)?',text):
        api.sendMessage(u'开始正常模式',chat['id']);
    

    if re.match(r'/join(@cdqzWerewolfBot)?',text):
        api.sendMessage(u'加入',chat['id']);

    """
    在这里搞事情
    """

def F_newMember(member,send_by,chat):

    print member
    print send_by
    print chat

    if not member.has_key('last_name'):
        member['last_name'] = ''
    if not member.has_key('first_name'):
        member['first_name'] = ''
   
    if member['id'] == 242058444:
        api.sendMessage(u'来来来,打狼人',chat['id'])
    else:
        api.sendMessage(u'欢迎'+member['last_name']+' '+member['first_name'] + u'进群,来一起打狼人吗',chat['id'])
    
    


def dealMessage():

    print 'dM ok'

    database.test += 1

    value = {'offset' : api.update_id}
    mess = api.work('/getupdates',value)

    if mess.has_key('result'):
        for tmp in mess['result']:
            if tmp.has_key('message'):
                mes = tmp['message']
                if mes.has_key('text'):
                    F_text(mes['text'],mes['from'],mes['chat'])

                if mes.has_key('new_chat_member'):
                    F_newMember(mes['new_chat_member'],mes['from'],mes['chat'])
    else:
        print "error, no 'result' "


