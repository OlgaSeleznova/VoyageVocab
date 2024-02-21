from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
import argparse
from flask import Flask, request, jsonify
from langchain_core.prompts import ChatPromptTemplate
import json

app = Flask(__name__)
@app.route('/chain', methods=['POST'])
def ollm():
    if request.method == 'POST':
        llm = Ollama(model="llama2:13b-chat")
        input = json.loads(request.data)
        answer = llm.invoke(f"You are a foreign language tutor. I'm travelling to {input['country']}. 
                            Which {input["phrases_num"]} phrases should I learn to {input['task']}?")
        return answer
    
