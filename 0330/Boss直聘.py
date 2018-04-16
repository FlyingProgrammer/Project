# coding: UTF-8
import json

import requests
import re

f=open(R'E:\bossIndex.html','w',encoding='utf-8')   #这句很吊
def buildSelect(li):
     return '[\s\S]*?'.join(li)

head='''
{"authority": "www.zhipin.com",
"method": "GET",
"path": "/c101280600-p100109/",
"scheme":"https",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding":"gzip,deflate,br",
"accept-language":"zh-CN,zh;q=0.9",
"cache-control":"max-age=0",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}'''

dicHead = json.loads(head)
print(dicHead)
sHtml = requests.get('https://www.zhipin.com/c101280600-p100109/',headers=dicHead).text
reJob =' <div class="job-title">(.*?)</div>'
reSalary='<span class="red">(\d+.*?)</span>'
reDetail='<p>([\u4e00-\u9fa5]+：.*?)</p>'
reInfo ='</h3>\s+<p></p>'
f.write(sHtml)
li = [reJob,reSalary,reDetail]
patSelect = buildSelect(li)
print(patSelect)
pat = re.compile(buildSelect(li),re.S)
#print(sHtml)
li = pat.findall(sHtml)

for x in li:
    print(x)