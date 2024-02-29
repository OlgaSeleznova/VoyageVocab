# VoyageVocab. Language Learning assistant for travel lovers

## Introduction
In this pet project I combined my main passions: AI, languages and traveling. 
While plannning a trip, I like to learn a few phrases to feel more comfortable while interracting with locals. 
The tool was built using two frameworks: Ollama for content generation and Gradio to build simple and interactive UI.  

## Installation
Create a new environment (I prefer conda): 
    `conda create -n myenv llm` 
    and then activate it: `conda activate llm`

### Ollama
1. Download Ollama via this link: https://ollama.com/download/mac
2. Install langchain-community:   
    `conda install langchain -c conda-forge` or `pip install langchain`   
    and then    
    `pip install langchain-community`   
3. Download a model, in this case mistral: `ollama run mistral`
The full list of available models is here: https://ollama.com/library
To check which models are available, run `ollama list`
### Gradio 
Install Gradio:
`pip install gradio`

### Whisper
Install whisper from GitHub:
`pip install git+https://github.com/openai/whisper.git`

## Usage
To use this app, run in terminal `python VoyageVocab.py`.      
Then follow the link to local URL, provided in the terminal. It's normally http://127.0.0.1:7860.  
1. Decide, what is the task. Do youu want to know how to order some food in the restaurant, buy a ticket or ask for direction.   
There are two options: *enter the text* or *record your voice*. Please, don't try to do both, because the app will choose the text.   
2. Choose the destination by clicking the relevant box (it's multiple choice and skipping this step will result in the error).   
3. Pick a number of phrases from 1 to 10.  
4. Finally, press the button "Generate" and check the answer.   


