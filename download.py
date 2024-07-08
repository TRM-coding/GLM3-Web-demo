from modelscope import snapshot_download
#do not use vpn,model will be saved in './glm4'
model_dir=snapshot_download("ZhipuAI/glm-4-9b-chat",cache_dir='./glm4')