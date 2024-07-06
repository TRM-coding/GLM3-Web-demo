import torch
# from modelscope import AutoModel,AutoTokenizer,snapshot_download
from transformers import AutoModel,AutoTokenizer
import os


from flask import Flask,request,jsonify
from LLMkernel import LLMkernel

app=Flask(__name__)
os.environ["CUDA_VISIBLE_DEVICES"]=','.join(map(str,[0,1]))
# use modelscope download the model.default dir : /root/.cache/modelscope
# model_dir=snapshot_download("ZhipuAI/chatglm3-6b",revision="v1.0.0")
# move the model to current dir,then use the model_dir to load the model
model_dir='./chatglm3-6b'
with torch.no_grad():
    LLM=AutoModel.from_pretrained(model_dir,trust_remote_code=True,device_map='auto').float().eval()

tokenizer=AutoTokenizer.from_pretrained(model_dir,trust_remote_code=True)
# LLM=LLM.eval()

@app.route("/kernel_chat",methods=["POST"])
def predict():
    json_data=request.get_json()
    print(json_data)
    kernel=LLMkernel(LLM,tokenizer)
    result=kernel.chat(json_data)
    print(result)
    return result
    

@app.route("/getbooks",methods=["POST"])
def getBooks():
    json_data=request.get_json()
    print(json_data)
    kernel=LLMkernel(LLM,tokenizer)
    result=kernel.getBooks(json_data)
    print(result)
    return result


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

# if __name__=="__main__":
#     predict()
#     print(torch.__version__)
# /root/.cache/modelscope/hub/._____temp/ZhipuAI/