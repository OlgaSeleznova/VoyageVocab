from flask import Flask, request, jsonify
from langchain_community.llms import Ollama


app = Flask(__name__)
@app.route('/ollm')
def ollm():
    llm = Ollama(model="llama2:13b-chat")
    input = request.args.get('query')
    answer = llm.invoke(f"I'm travelling to {input.country}. Which phrases should I learn to {input.task}?")
    return answer
