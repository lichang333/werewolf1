#coding:utf-8
import api
import database
import re
import cPickle as pickle

def CallEveryone(chat_id,title):
    
    callList = pickle.load(open('callList.secret','r'))
    
    if callList.has_key(chat_id) :
        text = u'有人在' + title + u'召唤你打狼人了'
        infor = u'已召唤'

        for user in callList[chat_id]:
            print user
            api.sendMessage(text,user[0])
            infor += ' ' + user[1] 


        print infor.encode('utf-8')
        api.sendMessage(infor,chat_id)
    else:
        print chat_id

def AddMe(chat_id,user):
    callList = pickle.load(open('callList.secret','r'))
    one = (user['id'], user['first_name'])
    if callList.has_key(chat_id):
        callList[chat_id].add(one)
    else:
        callList[chat_id] = set([one])

    pickle.dump(callList,open('callList.secret','w'))
    
    ret = api.sendMessage(u'添加成功',one[0]) 
    if ret == {}:
        api.sendMessage(one[1] + u',请先私bot',chat_id)
        print 'fail'
    else:
        print 'succ'


def F_text(text,send_by,chat):
    print unicode(text).encode('utf-8') , chat['id']
   #api.sendMessage(text,chat['id'])

    if re.match(r'/chaosGame(@cdqzWerewolfBot)?',text):
        api.sendMessage(u'开始混乱模式',chat['id']);

    
    if re.match(r'/normalGame(@cdqzWerewolfBot)?',text):
        api.sendMessage(u'开始正常模式',chat['id']);
    

    if re.match(r'/join(@cdqzWerewolfBot)?',text):
        api.sendMessage(u'加入',chat['id']);

    if re.match(r'/sad(@cdqzWerewolfBot)?',text):
        api.sendMessage(u'我赌五毛人不够',chat['id']);
        database.fail = 60
        database.chatId = chat['id'];

    if re.match(r'/calleveryone(@cdqzWerewolfBot)?',text):
        if chat.has_key('title'):
            CallEveryone(chat['id'],chat['title']); 
    
    if re.match(r'/addmetolist(@cdqzWerewolfBot)?',text):
        AddMe(chat['id'],send_by)
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


