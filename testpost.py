import requests
import json
import time

url="http://i-2.gpushare.com:40003/chat"

prompt="简单讲讲微积分"
dict={
    "msg":prompt,
    "temperature":0.5
}

json_obj=json.dumps(dict)
headers = {'Content-Type': 'application/json'}
since=time.time()
req=requests.post(url,data=json_obj,headers=headers)                                                                          

print(req.json())
print(f"响应时间：{time.time()-since}")


