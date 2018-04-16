import requests
import json
import re

def doRequest(url,i):
    print(url)
    r = requests.get(url)
    patName = re.compile('class="">\s+<span class="title">(.*?)</span>*<span class="rating_num" property="v:average">(\d+\.\d)</span> ', re.S)
    patScore = re.compile('<span class="rating_num" property="v:average">(\d+\.\d)</span>')
    print(r.text)
    listName = patName.findall(r.text)
    listScore = patScore.findall(r.text)
    print(len(listName))
    print(len(listScore))
    for j in range(len(listName)):
        print('{:<14}{:<14}'.format(listName[j], listScore[j]))


for i in range(1):
    url='https://movie.douban.com/top250?start='+str(1*25)+'&filter='
    doRequest(url,i)


