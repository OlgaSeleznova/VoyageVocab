from flask import Flask, request, jsonify
from langchain_community.llms import Ollama


app = Flask(__name__)
@app.route('/ollm')
def ollm():
    llm = Ollama(model="llama2")
    query = request.args.get('query')
    answer = llm.invoke(query)
    return answer

@app.route('/test', methods=['POST'])
def boo():
    if request.method == 'POST':
        username = request.form['username']
        # Process the username, e.g., save it to a database
        return f'Hello, {username}!'

# if __name__=='__main__':
#     parser = argparse.ArgumentParser()
#     args = parse_args(parser)
#     main(args)
    # "I want to learn 10 most frequent words in French for travelling with examples"