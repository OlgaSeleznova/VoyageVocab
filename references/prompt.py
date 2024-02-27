from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
import argparse
from flask import Flask, request, jsonify
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain




def ollm(topic, language):
    # if request.method == 'POST':
    llm = Ollama(model="llama2")
    # input = request.args.get('query')
    prompt = (
    PromptTemplate.from_template("Tell me a joke about {topic}")
            + ", make it funny"
            + "\n\nand in {language}")
    print(prompt)
    chain = LLMChain(llm=llm, prompt=prompt)
    answer = chain.invoke(topic=topic, language=language)
    return answer
    
ollm(topic="sports", language="russian")