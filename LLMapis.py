import torch
from modelscope import snapshot_download
import os

from transformers import AutoModel,AutoTokenizer

from flask import Flask,request,jsonify
from LLMkernel import LLMkernel

app=Flask(__name__)

model_dir="../models/glm4/ZhipuAI/glm-4-9b-chat"

#MULTI-GPU-DEPLOYMENT
#modelscope also has class AutoModel,but we need transformers.AutoModel to 
#achieve MULTI-GPU-DEPLOYMENT
os.environ["CUDA_VISIBLE_DEVICES"]=','.join(map(str,[0,1]))
with torch.no_grad():
    LLM=AutoModel.from_pretrained(model_dir,trust_remote_code=True,device_map='auto').float().eval()
tokenizer=AutoTokenizer.from_pretrained(model_dir,trust_remote_code=True)

@app.route("/kernel_chat",methods=["POST"])
def predict():
    json_data=request.get_json()
    print(json_data)
    kernel=LLMkernel(LLM,tokenizer)
    result=kernel.chat(json_data)
    print(result)
    # result=str(result)
    result={"respond":result}
    print(result)
    return jsonify(result)


@app.route("/getbooks",methods=["POST"])
def getBooks():
    json_data=request.get_json()
    print(json_data)
    kernel=LLMkernel(LLM,tokenizer)
    result=kernel.getBooks(json_data)
    result={"respond":result}
    print(result)
    return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
