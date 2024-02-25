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
def llm(task, country, number):
    llm = Ollama(model="mistral")
    lang = get_language(country, file="country_to_language.json")
    few_shot = examples(file="fewshot_learning.txt")
    context = f"You are a helpful assistant. You give an enumerated list of phrases. You answer concisely and only in {lang}."
    icl = f"For example, {few_shot}"
    query = f"I'm travelling to {country}. Which {number} most popular phrases should I learn to {task}?"
    phrases = llm.invoke(context+icl+query)    
    return phrases
    
def main():    
    demo = gr.Blocks()
    with gr.Blocks() as demo:
        gr.Markdown("# Assistant for Travelers")
        # gr.Markdown("Add text or audio to get the most popular phrases for your travel destination.")
        with gr.Row():
            with gr.Column():
                gr.Markdown("## Inputs: ")
                with gr.Row():
                    # gr.Markdown("### Text input: ")
                    # gr.Markdown("### Audio input: ")
                    # gr.Markdown("## Inputs: ")
                        # input_type = gr.Radio(["Text", "Audio"], label="Input type", info="Choose the input type")
                    with gr.Column():
                        gr.Markdown("### Text input: ")
                        task = gr.Textbox(info="What do you want to do?", label="Task", placeholder="order food, ask for directions, etc.")
                    with gr.Column():
                        gr.Markdown("### Audio input: ")
                        audio = gr.Audio(sources=["microphone"], label="Record your voice", type="filepath", max_length=10) 
                        stt = gr.Button("Transcribe audio")
                        task = gr.Textbox("Transcribed text will appear here.")
                        stt.click(fn=transcribe_audio, inputs=audio, outputs=task) 
                    with gr.Column():
                        country = gr.Radio(["France", "Germany", "Italy"], label="Location", info="Where are you travelling?")
                        num = gr.Slider(0, 10, value=5, step=1, info="How many phrases?", label="Number of phrases")
            with gr.Column():
                gr.Markdown("## Output: ")
                response = gr.Button("Generate response")
                out = gr.Textbox("Response will appear here.")
                response.click(fn=llm, inputs=[task, country, num], outputs=out)
            
    demo.launch(share=False, debug=True)


if __name__ == '__main__':
    main()