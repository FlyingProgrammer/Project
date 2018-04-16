import requests
import json
import re
f = open(r'E:/豆瓣Top250.txt', 'w')
def doRequest(url,i):
    print(url)
    r = requests.get(url)
    patName = re.compile('class="">\s+<span class="title">(.*?)</span>', re.S)
    patScore = re.compile('<span class="rating_num" property="v:average">(\d+\.\d)</span>')
    listName = patName.findall(r.text)
    listScore = patScore.findall(r.text)
    f.write('**********'+str(i*25+1)+'  To  '+str(i*25+25) +'**********\n\n')
   # for i in range(len(listName)):
        #print('{:<14}{:<14}'.format(listName[i], listScore[i]))

    for j in range(len(listName)):

        f.write(str(i*25+j+1)+'\t'+listScore[j]+'\t' +listName[j])
        f.write('\n')
    f.write('\n')

for i in range(10):
    url='https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    doRequest(url,i)
f.close()


