import requests

r= requests.get('http://ip.taobao.com/service/getIpInfo.php')
print(r.status_code)