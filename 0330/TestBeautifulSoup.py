#coding:utf_8
from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<table>
<tr><td>f</td>
</tr>
</table>
<div><p class="title" name="dromouse"><b>The Dormouse's story</b></p></div>

<p class="story">...</p>
"""
bs = BeautifulSoup(open(r'E:\py\bossIndex.html',encoding='utf-8'),"html5lib")
bs = BeautifulSoup(html,"html5lib")
#print(len(bs.head.children))
for x in bs.body.contents:
    print(x)
for x in bs.body.children:
    print(x)

for x in bs.body.descendants:
    print(x)