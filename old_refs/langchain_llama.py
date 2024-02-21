from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
import argparse
from flask import Flask, request, jsonify
from langchain_core.prompts import ChatPromptTemplate

# NOT WORKING !!

app = Flask(__name__)
@app.route('/chain', methods=['POST'])
def ollm():
    if request.method == 'POST':
        llm = Ollama(model="llama2")
        input = request.args.get('query')
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a french tutor. You give a simple conversation in french about the topic {input}."),
            ("user", "{input}")
        ])
        chain = prompt | llm 
        answer = chain.invoke({"input": input})
        return answer
    
