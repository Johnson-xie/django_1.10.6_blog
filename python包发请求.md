## urllib带params和headers发起请求（python3）  
```  
import urllib.parse
import urllib.request
import ssl
from pprint import pprint
import json

HEADERS = {'PRIVATE-TOKEN': 'HSHfzhx4KWMx2xanPm_c'}
params = {'more_info': 'true', 'page': '1', 'per_page': '200', 'ref_name': 'master'}

url_para = urllib.parse.urlencode(params)


url = r'https://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/repository/commits/'
full_url = url + '?' + url_para

context = ssl._create_unverified_context()

request = urllib.request.Request(full_url, headers=HEADERS)

ret = urllib.request.urlopen(request)

data = ret.read().decode('utf-8')
data = json.loads(data)
pprint(data)
print(len(data))
print(type(data))
```  

## request发起带params和headers请求  
```  
import requests
from pprint import pprint

HEADERS = {'PRIVATE-TOKEN': 'HSHfzhx4KWMx2xanPm_c'}
params = {'more_info': 'true', 'page': '1', 'per_page': '200', 'ref_name': 'master'}
# web库
url = r'https://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/repository/commits/'


HTTPS_CRT_FILE = r"D:\wokroom_door\web\mysite\config\ca-bundle.crt"

# ret = requests.get(url, params=params, headers=HEADERS, verify=HTTPS_CRT_FILE, timeout=60)
ret = requests.get(url, params=params, headers=HEADERS, timeout=60)
pprint(ret.json())
```  

# urllib发起post请求  
```  
import urllib.request
import urllib.parse

url = "http://johnson.com/api/email/send/"
data = {
    "to": "xieqiang6@huawei.com,chenshuanglong1@huawei.com",
    "subject": "【击鼓传花dts提单订阅】",
    "content": "<html><h1>hello world</h1></html>",
    "content_type": "html"
}
textmod = urllib.parse.urlencode(data).encode(encoding='utf-8')
request = urllib.request.Request(url)
ret = urllib.request.urlopen(request, data=textmod)
```  

