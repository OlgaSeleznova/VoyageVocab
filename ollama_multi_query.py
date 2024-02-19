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
        phrases = llm.invoke(f"I'm travelling to {input['country']}. Which phrases should I learn to {input['task']}?")
        dialogue = llm.invoke(f"Please use the following phrases {phrases} to create a dialogue about the topic {input['task']}")
        test = llm.invoke(f"Create a list of possibly new words from this dialogue with translations. {dialogue}. Then create a multiple choice quiz for these words.")
        return f"""You may need the following phrases to {input['task']} in {input['country']}: //
        /n/n {phrases} /n/n Here's a sample dialogue for the phrases /n/n {dialogue} //
        /n/n Now let's practice. {test}"""
    
