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


def get_examples(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    audio = whisper.load_audio(audio_file,sr=16000)
    audio_tensor = torch.from_numpy(audio).to(torch.float32)
    result = model.transcribe(audio_tensor, fp16=False)['text']
    return result


def match_task(text, audio):
    if text and audio:
        return text
    elif text:
        return text
    elif audio:
        return transcribe_audio(audio)
    else:
        return ReferenceError("No input provided.")
    

def llm(task, country, number):
    llm = Ollama(model="mistral")
    
    lang = get_language(country, file="country_to_language.json")
    few_shot = get_examples(file="fewshot_learning.txt")
    context = f"You are a helpful assistant. You give an enumerated list of phrases. You answer concisely and only in {lang}."
    icl = f"For example, {few_shot}"
    query = f"I'm travelling to {country}. Which {number} most popular phrases should I learn to {task}?"
    phrases = llm.invoke(context+icl+query)    
    return phrases
    

def main():    
    demo = gr.Blocks()
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        # with gr.Column():
        gr.Markdown("# Assistant for Travelers")
        gr.Markdown("### What do you want to do: order food in the restaurant, ask for direction, buy tickets?")
        gr.Markdown("### Record audio or enter text.")
        with gr.Row():
            with gr.Column():
                text = gr.Textbox(label="Enter text", placeholder="order food, ask for directions, etc.")
            with gr.Column():
                audio = gr.Audio(sources=["microphone"], label="Record your voice", type="filepath", max_length=10) 
            #     stt = gr.Button("Transcribe audio")
            # with gr.Column():
            #     task = gr.Textbox()
            #     stt.click(fn=transcribe_audio, inputs=audio, outputs=task) 
        with gr.Row():
            with gr.Row():
                country = gr.Radio(["France", "Germany", "Italy"], label="Location", info="Where are you travelling?")
                num = gr.Slider(0, 10, value=5, step=1, info="How many phrases?", label="Number of phrases")    
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    response = gr.Button("Generate response", variant="primary")
                    clear = gr.Button("Clear")
                out = gr.Textbox(label="Response")
                task = match_task(text, audio)
                response.click(fn=llm, inputs=[task, country, num], outputs=out)
                
    demo.launch(share=False, debug=True)


if __name__ == '__main__':
    main()