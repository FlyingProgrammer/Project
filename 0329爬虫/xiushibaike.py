#coding:utf-8
import requests
import re
r=requests.get('https://www.qiushibaike.com/hot')
htmls = r.text
#print(htmls)

pat = re.compile('<div class="content">\s+<span>\s+(.*?)</span>',re.S)
l=pat.findall(htmls)
f= open(r'E:\xiushi.txt','w+')
for x in l:
    x=x.replace('<br/>','').replace('<br/>','')
    if(x.__len__()>20):
        f.write(x)
f.close()