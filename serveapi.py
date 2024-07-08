from flask import request, jsonify,Flask

import json
import requests

app=Flask(__name__)




@app.route("/chat",methods=['POST'])
def chat():
    data=request.get_json()
    prompt=data['msg']
    temp=data['temperature']
    url="http://127.0.0.1:5000/kernel_chat"
    json_dt={
        "prompt":prompt,
        "temperature":temp
    }
    json_obj=json.dumps(json_dt)
    headers = {'Content-Type': 'application/json'}
    respond=requests.post(url,data=json_obj,headers=headers) 
    print(respond)
    return jsonify(respond.json())

@app.route("/book",methods=["POST"])
def book():
    data=request.get_json()
    prompt=data['msg']
    temp=data['temperature']
    url="http://127.0.0.1:5000/getbooks"
    json_dt={
        "prompt":prompt,
        "temperature":temp
    }
    json_obj=json.dumps(json_dt)
    headers = {'Content-Type': 'application/json'}
    respond=requests.post(url,data=json_obj,headers=headers) 
    
    return jsonify(respond.json())




if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080)