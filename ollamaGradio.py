from langchain_community.llms import Ollama
import gradio as gr
import json
import whisper
import numpy as np
import torch, torchaudio

def get_language(country, file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data[country]


def examples(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    audio = whisper.load_audio(audio_file,sr=16000)
    audio_tensor = torch.from_numpy(audio).to(torch.float32)
    result = model.transcribe(audio_tensor, fp16=False)['text']
    return result

#CHECK THAT AUDIO INPUT EXISTS
def llm( task, recording, country, number):
    transcription = transcribe_audio(recording)
    if transcription is None:
        transcription = "Audio isn't clear. Please try again."
    else:
        task = transcription
    llm = Ollama(model="mistral")
    lang = get_language(country, file="country_to_language.json")
    few_shot = examples(file="fewshot_learning.txt")
    context = f"You are a helpful assistant. You give an enumerated list of phrases. You answer concisely and only in {lang}."
    icl = f"For example, {few_shot}"
    query = f"I'm travelling to {country}. Which {number} most popular phrases should I learn to {task}?"
    phrases = llm.invoke(context+icl+query)    
    return phrases
    
def main():    
    demo = gr.Interface(fn=llm, 
                        inputs=[
                            gr.Textbox(info="What do you want to do?", label="Task", placeholder="order food, ask for directions, etc."),
                            gr.Audio(sources=["microphone"], label="Record your voice", type="filepath", max_length=3),
                            gr.Radio(["France", "Germany", "Italy"], label="Location", info="Where are you travelling?"), 
                            gr.Slider(0, 10, value=5, step=1, info="How many phrases?", label="Number of phrases"),
                            ], 
                        description="Add text or audio to get the most popular phrases for your travel destination.",
                        title="Assistant for Travelers",
                        # examples=[["order food in the restaurant", "buy a ticket for the train", "ask for directions", "find museum" ,"buy a dress"]],
                        outputs=["text"])
    # gr.Markdown("Please ")
    demo.launch(share=False, debug=True)


if __name__ == '__main__':
    main()