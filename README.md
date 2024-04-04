# VoyageVocab. Language Learning assistant for travellers

## Introduction
In this project, I combined my main passions: AI, languages and travelling. 
This application receives textual or audio input to generate phrases in foreign languages for specific tasks: ordering food/ buying a ticket, etc.  
The tool was built using the following technologies: Ollama for content generation, Whisper for speech recognition and Gradio to build simple and interactive UI.

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
1. Decide, what is the task. Do you want to know how to order some food in the restaurant, buy a ticket or ask for directions.   
There are two options: *enter the text* or *record the voice*. In case of both text and audio entered, text will be chosen.   
2. Choose the destination by clicking the relevant box (it's multiple choice and skipping this step will result in the error).   
3. Pick a number of phrases from 1 to 10.  
4. Finally, press the button "Generate" and check the answer.   


