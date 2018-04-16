# -*- coding:utf-8 -*-
keyList = ['FListClassName','FVisible',' FLookUpClassID','FLookUpList','FSRCFieldName','FSRCTableName','FSRCTableNameAs',
        'FDSPFieldName','FFNDFieldName','FValueLocation','FFilterGroup','FDspColType','FEditlen','FValuePrecision','FSaveRule',
        'FKeyWord','FCondition','FLock','FSum','FPrec','FScale','FLayer','FLoadAction','FUnControl','FSourceType']
headList=[]
def makeSql(str,row):
    lvalue = str.split('\t')
    strSql = 'update ICClassTableInfo set '
    n=0
    while n<len(lvalue):
        if lvalue[n].isdigit():
            strTmp = keyList[n] + ' = ' + lvalue[n]+','
        else:
            strTmp = keyList[n] + ' = \'' + lvalue[n] + '\','
        strSql += strTmp
        n+=1
    strSql=strSql[0:len(strSql)-1]
    strSql += ' Where FFieldName = \''+headList[row] + '\'\n'
    fr = open(r'C:\Users\zh_tu\Desktop\res.txt', 'a')
    fr.write(strSql)
    return strSql

fv=open(r'C:\Users\zh_tu\Desktop\value.txt','r')
fh=open(r'C:\Users\zh_tu\Desktop\head.txt','r')
headList = fh.read().split('\n')
strResult=''
row=0
while row<len(headList):
    strResult += makeSql(fv.readline().replace('\n',''),row)
    row+=1

#print(strResult)
