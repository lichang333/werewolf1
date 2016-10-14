#coding:utf-8
import time
from dealMessage import dealMessage
from dealTimeCounter import dealTimeCounter

print 'START:',time.strftime('%Y-%m-%d %H:%M:%S')

while 1:
	dealMessage()       #接受消息,处理回应消息方面的操作
        dealTimeCounter()   #计数器减一,处理和倒计时有关的操作
        time.sleep(0.8)


