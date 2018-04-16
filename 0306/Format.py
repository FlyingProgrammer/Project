# -*- coding:utf-8 -*-
headList=[]
fh=open(r'C:\Users\zh_tu\Desktop\head1.txt','r')
strResult=''
row=0
while row<53:
    strResult += '\''+ fh.readline().replace('\n','')+'\','
    row+=1

print(strResult)
