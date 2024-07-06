import pymysql
import torch
from modelscope import AutoModel,AutoTokenizer,snapshot_download
import pymysql
from flask import jsonify
class LLMkernel:
    def __init__(self,llm,tokenizer):
        self.LLM=llm
        self.tokenizer=tokenizer
    
    def getBooks(self,json_data):
        content=json_data['prompt']
        conn=pymysql.connect(
            host="localhost",
            user="root",
            passwd="123",
            database="WIFI"
        )
        cursor=conn.cursor()
        sql="select * from book"
        cursor.execute(sql)
        booklist=cursor.fetchall()
        booklist=str(booklist)
        print(booklist)

        # template=f"""作为一位专业的图书检索专家，现在用户提出这样的检索需求：{content}，
        # 已知，现在图书馆中有这些书籍：{booklist}。请你根据用户需求，剔除不相关的书籍内容，把相关的书籍内容返回成列表。如果没有相关的书籍，请你输出：无书籍信息"""
        # print("正在响应...")
        # result,history=self.LLM.chat(self.tokenizer,template,history=[],temperature=0.1)
        # print(result)
        # print("正在响应...")
        # template=f"""作为一名专业的信息清洗专家，你从来不会出错。现在有一个大语言模型的输出信息{result},你需要
        # 将里面的书籍列表抽取出来，并用json格式 "编号":"书籍名" 表示这些信息。如果大模型没有检索到书籍信息，请你输出空的json对象"""
        # result,history=self.LLM.chat(self.tokenizer,template,history=[],temperature=0.1)
        # print(result)
        # print("正在响应...")
        # template=f"""
        # 作为一名专业的信息清洗专家，你从来不会出错，现在有一个大语言模型的输出信息{result},你需要将里面
        # 的json信息抽取出来，并输出。请确保你的输出只能由json信息，不能包含如“这是你的答案”这样的交互信息"""

        template=f"""作为一位专业的图书检索专家，现在用户提出这样的检索需求：{content}，
        请你从{booklist}中检索符合用户要求：{content}的书籍，并生成一个列表，这个列表应该按照和用户需求的相关性，从高到低排序。返回前5本书给用户。注意，你返回的书籍必须来源于{booklist},不能返回除了{booklist}之外的书籍。如果没有，则告诉用户：“图书馆中没有这样的书” 并且，一本也不要返回！"""

        result,history=self.LLM.chat(self.tokenizer,template,history=[],temperature=0.9)
        respond_json={"respond":f"{result}"}
        print(result)
        return jsonify(respond_json)
    

    def chat(self,json_data):
        prompt=json_data['prompt']
        print("正在响应...")
        result,history=self.LLM.chat(self.tokenizer,prompt,history=[])
        result=str(result)
        respond_json={"respond":f"{result}"}
        print(result)
        return jsonify(respond_json)