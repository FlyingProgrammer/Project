# -*-coding:utf-8 -*-
dic={}
sumyear=1;
sumDay=sumyear*365
rate7=4.1200
sum_money=0
sum_shouyi=0
for day in range(1,sumDay+1):
    sum_money+=(day+ sum_money *rate7/36500)
    sum_shouyi = sum_money *rate7/36500 + sum_shouyi;
    dic[day]=(sum_money,sum_shouyi)
def printMoney(day):
    print("第%d天余额：%f元，收益累计：%f元"%(day,dic[day][0],dic[day][1]))
for x in range(1,sumDay+1,1):
    printMoney(x)


