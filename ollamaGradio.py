from langchain_community.llms import Ollama
import gradio as gr

def main(country, task, number):
    llm = Ollama(model="mistral")
    context = "You are a helpful assistant. You give enumerated list of phrases. Your answer is strictly. You give only phrases in foreign language and an english translation in brackets. Numerals are not included in the query."
    query = f"I'm travelling to {country}. Which {number} most popular phrases should I learn to {task}?"
    phrases = llm.invoke(context+query)    
    return phrases
    
    
demo = gr.Interface(fn=main, 
                    inputs=[
                        gr.Radio(["France", "Germany", "Italy"], label="Location", info="Where are you travelling?"), 
                        gr.Textbox(info="What do you want to do?"),
                        gr.Slider(0, 10, value=5, step=1,info="How many phrases?")
                        ], 
                    outputs=["text"])
demo.launch(share=True)
