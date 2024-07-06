import requests
import json
import time

# url to the server
# url="http://i-2.gpushare.com:35150/book"



json_dt={"msg":"给我找找有关物理的书"}

json_obj=json.dumps(json_dt)
headers = {'Content-Type': 'application/json'}
since=time.time()
respond=requests.post(url,data=json_obj,headers=headers)                                                                          

# print(response.json())
print(f"响应时间：{time.time()-since}")


