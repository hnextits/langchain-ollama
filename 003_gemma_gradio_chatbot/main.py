# Ollama 모델 로드 및 테스트
from langchain_community.chat_models import ChatOllama
import gradio as gr


model = ChatOllama(model="lamma3.1", temperature=0)


def echo(message, history):
    response = model.invoke(message)
    return response.content

demo = gr.ChatInterface(fn=echo, title="Llama Bot")
demo.launch()
