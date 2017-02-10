# werewolf1
狼人bot第一版

一个由cdqz ingresser共同进行的telegram 上的狼人杀bot

for developer:
    api.py应该不用动,主要是在dealMessage.py的F_text函数里面和dealTimeCounter里面写东西.
    各种倒计时的东西,群ID玩家名单等东西在database.py里面定义,倒计时的计数器在dealTimeCounter.py里面每次减一.

#Avalon Vol.1
    TodoList:
        基本的角色实现
        选择队员
        发言(应该没法挨个发言，做成(固定时间/所有人点下结束发言才结束)自由讨论比较好)
        没了。。实现难度确实远远低于狼人
