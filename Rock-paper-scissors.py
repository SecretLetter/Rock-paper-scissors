

#==========START==========
#导入模块
print ("正在导入模块……")
import time
import random

#初始化变量
print ("正在初始化……")
p1point=0
p2point=0
ready=0
total_rounds=0
now_rounds=0
need_teach=0
p1num=0
p2num=0
error=0

#欢迎
print ( "欢迎来到剪刀石头布python单机版！")
time.sleep (1.5)

#询问玩家是否需要教程
print ("请问您是否需要教程呢？")
time.sleep (1.5)
need_teach=input ("需要请输入 1 ，否则请输入其他任意字符 ")
if need_teach=="1":
    #介绍规则
    print ("游戏规则与石头剪刀布大同小异，")
    time.sleep (1.5)
    print ( "游戏开始后，需要玩家输入游戏的总局数。")
    time.sleep (1.5)
    print ( "然后，p1与p2分别输入代表石头、剪刀、布的数字来对决。")
    time.sleep (1.5)
    print ( "其中 “1” 代表剪刀， “2” 代表石头，而 “3” 则代表布")
    time.sleep (1.5)
    print ( "待p1与p2输入完成后，系统会以 “石头胜剪刀，剪刀胜布，布胜石头” 的规则判定获胜方")
    time.sleep (1.5)
    print ( "当有一方获得半数以上的胜利时，游戏会结束并且宣布赢家。")
    time.sleep (1.5)

#等待玩家准备开始游戏
    ready=input ("以上是游戏的规则，准备好后请输入 1 确认开始游戏 ")
else:
    ready=input ("已为您跳过教程，准备好后请输入 1 确认开始游戏 ")
while ready != "1": #判断玩家是否输入正确
    print ("请输入 1 确认开始游戏，不需要加空格、引号之类，请确认是否输入正确")
    time.sleep (1.5)
    ready=input ("请输入 1 确认开始游戏 ")

#非常重要的TIP
print ("********************")
print ("游戏前的小tip")
print ("********************")
print ("注意：输入时按一次数字一次回车就好，不要多按！")
print ("注意：输入时按一次数字一次回车就好，不要多按！")
print ("注意：输入时按一次数字一次回车就好，不要多按！")
print ("重要的事情说三遍！")
print ("********************")
time.sleep (5)

#获得总局数
total_rounds=input ("请输入游戏的总局数：") #要求玩家输入总局数
while True:
    if not total_rounds.isdigit(): #判断输入是否为纯数字
        total_rounds=input ("请输入有效的 数字 ：") #要求玩家重新输入
    else:
        total_rounds=int(total_rounds)
        if total_rounds<=0: #判断输入是否小于等于0
            total_rounds=input ("请输入有效的 不小于等于0的 数字：") #要求玩家重新输入
        else:
            break #输入符合要求，跳出判断循环

#开始游戏
def point(): #定义播报分数函数
    global p1point
    global p2point
    global now_rounds
    print ("现在p1的分数为",p1point,"，p2的分数为",p2point,"，目前已完成",now_rounds,"局。")
def pk(p1num,p2num): #定义判定函数
    global now_rounds
    global p1point
    global p2point
    if p1num==1 and p2num==2: #p1剪刀，p2石头
        now_rounds+=1
        p2point+=1
        print ("p1出了剪刀，p2出了石头，本局p2获胜！")
    elif p1num==1 and p2num==3: #p1剪刀，p2布
        now_rounds+=1
        p1point+=1
        print ("p1出了剪刀，p2出了布，本局p1获胜！")
    elif p1num==2 and p2num==1: #p1石头，p2剪刀
        now_rounds+=1
        p1point+=1
        print ("p1出了石头，p2出了剪刀，本局p1获胜！")
    elif p1num==2 and p2num==3: #p1石头，p2布
        now_rounds+=1
        p2point+=1
        print ("p1出了石头，p2出了布，本局p2获胜！")
    elif p1num==3 and p2num==1: #p1布，p2剪刀 
        now_rounds+=1
        p2point+=1
        print ("p1出了布，p2出了剪刀，本局p2获胜！")
    elif p1num==3 and p2num==2: #p1布，p2石头 
        now_rounds+=1
        p1point+=1
        print ("p1出了布，p2出了石头，本局p1获胜！")
    elif p1num==p2num: #p1p2决定相同时
        if p1num==1: #都出剪刀
            print ("p1与p2都出了剪刀，本局不计分数，不计总局数。")
        elif p1num==2: #都出石头
            print ("p1与p2都出了石头，本局不计分数，不计总局数。")
        elif p1num==3: #都出布
            print ("p1与p2都出了布，本局不计分数，不计总局数。")
print("游戏开始")
time.sleep (1.5)
while not ((now_rounds==total_rounds) or (p1point==int(total_rounds/2+1)) or (p2point==int(total_rounds/2+1))): #如没有人达到获胜要求则循环游戏部分
    p1num=input ("请p1选择要出的物品，1 代表剪刀， 2 代表石头， 3 代表布 ：") #询问玩家要出的物品
    while True:
        if not p1num.isdigit(): #判断输入是否为纯数字
            error+=1 #输入错误次数加1
            print ("输入错误，您输入的不是纯数字。")
            time.sleep (1.5)
            if error!=5: #判断输入错误次数是否达到五次
                print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
            elif error==5:
                print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                p1num=random.randint (1,3) #随机选择剪刀石头布
                error=0 #初始化error变量
                time.sleep (1.5)
                if p1num==1:
                    print ("为您随机选择了剪刀。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p1num==2:
                    print ("为您随机选择了石头。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p1num==3:
                    print ("为您随机选择了布。")
                    break #播报并跳出循环
                    time.sleep (1.5)
            time.sleep (1.5)
            p1num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
        else:
            p1num=int(p1num)
            if p1num!=1 and p1num!=2 and p1num!=3: #判断输入是否为1或2或3
                error+=1 #输入错误次数加1
                print ("输入错误，您输入的数字不是1、2、3中的任何一个。")
                time.sleep (1.5)
                if error!=5: #判断输入错误次数是否达到五次
                    print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
                elif error==5:
                    print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                    p1num=random.randint (1,3) #随机选择剪刀石头布
                    error=0 #初始化error变量
                    time.sleep (1.5)
                    if p1num==1:
                        print ("为您随机选择了剪刀。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p1num==2:
                        print ("为您随机选择了石头。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p1num==3:
                        print ("为您随机选择了布。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                time.sleep (1.5)
                p1num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
            else:
                error=0
                break #输入符合要求，跳出判断循环
    p2num=input ("请p2选择要出的物品，1 代表剪刀， 2 代表石头， 3 代表布 ：") #询问玩家要出的物品
    while True:
        if not p2num.isdigit(): #判断输入是否为纯数字
            error+=1 #输入错误次数加1
            print ("输入错误，您输入的不是纯数字。")
            time.sleep (1.5)
            if error!=5: #判断输入错误次数是否达到五次
                print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
            elif error==5:
                print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                p2num=random.randint (1,3) #随机选择剪刀石头布
                error=0 #初始化error变量
                time.sleep (1.5)
                if p2num==1:
                    print ("为您随机选择了剪刀。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p2num==2:
                    print ("为您随机选择了石头。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p2num==3:
                    print ("为您随机选择了布。")
                    break #播报并跳出循环
                    time.sleep (1.5)
            time.sleep (1.5)
            p2num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
        else:
            p2num=int(p2num)
            if p2num!=1 and p2num!=2 and p2num!=3: #判断输入是否为1或2或3
                error+=1 #输入错误次数加1
                print ("输入错误，您输入的数字不是1、2、3中的任何一个。")
                time.sleep (1.5)
                if error!=5: #判断输入错误次数是否达到五次
                    print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
                elif error==5:
                    print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                    p2num=random.randint (1,3) #随机选择剪刀石头布
                    error=0 #初始化error变量
                    time.sleep (1.5)
                    if p2num==1:
                        print ("为您随机选择了剪刀。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p2num==2:
                        print ("为您随机选择了石头。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p2num==3:
                        print ("为您随机选择了布。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                time.sleep (1.5)
                p2num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
            else:
                error=0
                break #输入符合要求，跳出判断循环
    pk(p1num,p2num) #判定
    time.sleep (1.5)
    point() #播报分数

#如果游戏局数达到规定值时双方平分，进行加时赛
if p1point==p2point:
    print ("游戏局数已达到规定值,但双方平分，开始进行加时赛。")
    time.sleep (1.5)
    p1num=input ("请p1选择要出的物品，1 代表剪刀， 2 代表石头， 3 代表布 ：") #询问玩家要出的物品
    while True:
        if not p1num.isdigit(): #判断输入是否为纯数字
            error+=1 #输入错误次数加1
            print ("输入错误，您输入的不是纯数字。")
            time.sleep (1.5)
            if error!=5: #判断输入错误次数是否达到五次
                print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
            elif error==5:
                print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                p1num=random.randint (1,3) #随机选择剪刀石头布
                error=0 #初始化error变量
                time.sleep (1.5)
                if p1num==1:
                    print ("为您随机选择了剪刀。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p1num==2:
                    print ("为您随机选择了石头。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p1num==3:
                    print ("为您随机选择了布。")
                    break #播报并跳出循环
                    time.sleep (1.5)
            time.sleep (1.5)
            p1num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
        else:
            p1num=int(p1num)
            if p1num!=1 and p1num!=2 and p1num!=3: #判断输入是否为1或2或3
                error+=1 #输入错误次数加1
                print ("输入错误，您输入的数字不是1、2、3中的任何一个。")
                time.sleep (1.5)
                if error!=5: #判断输入错误次数是否达到五次
                    print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
                elif error==5:
                    print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                    p1num=random.randint (1,3) #随机选择剪刀石头布
                    error=0 #初始化error变量
                    time.sleep (1.5)
                    if p1num==1:
                        print ("为您随机选择了剪刀。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p1num==2:
                        print ("为您随机选择了石头。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p1num==3:
                        print ("为您随机选择了布。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                time.sleep (1.5)
                p1num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
            else:
                error=0
                break #输入符合要求，跳出判断循环
    p2num=input ("请p2选择要出的物品，1 代表剪刀， 2 代表石头， 3 代表布 ：") #询问玩家要出的物品
    while True:
        if not p2num.isdigit(): #判断输入是否为纯数字
            error+=1 #输入错误次数加1
            print ("输入错误，您输入的不是纯数字。")
            time.sleep (1.5)
            if error!=5: #判断输入错误次数是否达到五次
                print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
            elif error==5:
                print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                p2num=random.randint (1,3) #随机选择剪刀石头布
                error=0 #初始化error变量
                time.sleep (1.5)
                if p2num==1:
                    print ("为您随机选择了剪刀。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p2num==2:
                    print ("为您随机选择了石头。")
                    break #播报并跳出循环
                    time.sleep (1.5)
                elif p2num==3:
                    print ("为您随机选择了布。")
                    break #播报并跳出循环
                    time.sleep (1.5)
            time.sleep (1.5)
            p2num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
        else:
            p2num=int(p2num)
            if p2num!=1 and p2num!=2 and p2num!=3: #判断输入是否为1或2或3
                error+=1 #输入错误次数加1
                print ("输入错误，您输入的数字不是1、2、3中的任何一个。")
                time.sleep (1.5)
                if error!=5: #判断输入错误次数是否达到五次
                    print ("您已输入错误",error,"次，当您输入错误达5次时，系统将随机为您选择剪刀、石头或布。")
                elif error==5:
                    print ("您已输入错误达5次，为您随机选择剪刀石头布中……")
                    p2num=random.randint (1,3) #随机选择剪刀石头布
                    error=0 #初始化error变量
                    time.sleep (1.5)
                    if p2num==1:
                        print ("为您随机选择了剪刀。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p2num==2:
                        print ("为您随机选择了石头。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                    elif p2num==3:
                        print ("为您随机选择了布。")
                        break #播报并跳出循环
                        time.sleep (1.5)
                time.sleep (1.5)
                p2num=input ("请输入有效的 数字 ，1 代表剪刀， 2 代表石头， 3 代表布 ：") #要求玩家重新输入
            else:
                error=0
                break #输入符合要求，跳出判断循环
    pk(p1num,p2num) #判定
    time.sleep (1.5)
    point() #播报分数

#游戏结束
if p1point>p2point:
    print("本次游戏结束，本次游戏的赢家是p1!")
elif p2point<p1point:
    print("本次游戏结束，本次游戏的赢家是p2!")
time.sleep (1.5)
print("程序结束")
#==========END==========