from langchain_community.llms import Ollama
import argparse
from flask import Flask, request, jsonify



def main(a):
    llm = Ollama(model=a.model)
    print(llm.invoke(a.query))


def parse_args(parser):
    parser.add_argument('query', type=str)
    parser.add_argument('--model', type=str, default="llama2")
    p = parser.parse_args()
    return p


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    args = parse_args(parser)
    main(args)
    
    