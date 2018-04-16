import requests
import re

f=open(R'E:\双色球.txt','w')
r=requests.get('http://datachart.500.com/ssq/history/history.shtml')
r=requests.get('http://datachart.500.com/ssq/history/newinc/history.php?start=1&end=18035')
#print(r.text)
patNum =re.compile('<tr class="t_tr1"><!--<td>2</td>--><td>(\d+)</td><td class="t_cfont2">(\d+)</td><td class="t_cfont2">(\d+)</td><td class="t_cfont2">(\d+)</td><td class="t_cfont2">(\d+)</td><td class="t_cfont2">(\d+)</td><td class="t_cfont2">(\d+)</td><td class="t_cfont4">(\d+)</td>',re.S)

lr=patNum.findall(r.text)
for t in lr:
    f.write("期数:")
    for num in t:
        f.write(str(num)+'\t')
    f.write('\n')
f.close()

#<tr class="t_tr1"><!--<td>2</td>--><td>18035</td><td class="t_cfont2">07</td><td class="t_cfont2">10</td><td class="t_cfont2">11</td><td class="t_cfont2">17</td><td class="t_cfont2">23</td><td class="t_cfont2">28</td><td class="t_cfont4">15</td><td class="t_cfont4">&nbsp;</td><td>856,009,608</td><td>6</td><td>8,809,507</td><td>289</td><td>98,862</td><td>350,309,396</td><td>2018-03-29</td></tr>