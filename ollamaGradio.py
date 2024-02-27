from langchain_community.llms import Ollama
import gradio as gr
import json
import whisper
import torch


#function to load convert name of the country to the language spoken in that country
def get_language(country, file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data[country]


#function to load examples of phrases for few shot learning
def get_examples(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


#function to transcribe audio to text using whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    audio = whisper.load_audio(audio_file,sr=16000)
    audio_tensor = torch.from_numpy(audio).to(torch.float32)
    result = model.transcribe(audio_tensor, fp16=False)['text']
    return result


#function to match the task to the input provided: audio or text
def match_task(text, audio):
    if text and audio:
        return text
    elif text:
        return text
    elif audio:
        return transcribe_audio(audio)
    else:
        return ReferenceError("No input provided.")


#function to generate phrases for the user
def llm(task, country, number):
    llm = Ollama(model="mistral")
    lang = get_language(country, file="utils/country_to_language.json")
    few_shot = get_examples(file="utils/fewshot_learning.txt")
    context = f"You are a helpful assistant. You give an enumerated list of phrases. You answer concisely and only in {lang}."
    icl = f"For example, {few_shot}"
    query = f"I'm travelling to {country}. Which {number} most popular phrases should I learn to {task}?"
    phrases = llm.invoke(context+icl+query)    
    return phrases
    

#function to launch the application
def main():    
    demo = gr.Blocks()
    #create a gradio interface
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("# Assistant for Travelers")
        gr.Markdown("### What do you want to do: order food in the restaurant, ask for direction, buy tickets?")
        gr.Markdown("### Record audio or enter text.")
        #create a row with two columns
        with gr.Row():
            with gr.Column():
                text = gr.Textbox(label="Enter text", placeholder="order food, ask for directions, etc.")
            with gr.Column():
                audio = gr.Audio(sources=["microphone"], label="Record your voice", type="filepath", max_length=10) 
        # create a row with two blocks
        with gr.Row():
            country = gr.Radio(["France", "Germany", "Italy"], label="Location", info="Where are you travelling?")
            num = gr.Slider(0, 10, value=5, step=1, info="How many phrases?", label="Number of phrases")    
        #create a row with two buttons
        with gr.Row():
            with gr.Column():
                response = gr.Button("Generate response", variant="primary")
            with gr.Column():
                clear = gr.Button("Clear")
        #create a row for response
        with gr.Row():
            out = gr.Textbox(label="Response")
            task = match_task(text, audio)
        response.click(fn=llm, inputs=[task, country, num], outputs=out) 
        gr.ClearButton.add(clear, [text, audio, country, num, out])   
    demo.launch(share=False, debug=True)


if __name__ == '__main__':
    main()