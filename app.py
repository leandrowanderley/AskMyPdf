import os
from dotenv import load_dotenv
import gradio as gr
from src.pdf_processor import extract_text_from_pdf
from src.text_splitter import split_text
from src.vectorstore import create_vectorstore
from src.question_answerer import answer_question

load_dotenv()

def main(pdf_path, question):
    """
    Função principal para executar o aplicativo de perguntas e respostas sobre PDF.
    """
    with open("apikey.txt", "r") as f:
        gemini_api_key = f.read().strip()
    if not gemini_api_key:
        return "Erro: Chave da API do Gemini não encontrada na variável de ambiente. Por favor, configure a variável de ambiente GEMINI_API_KEY."

    # Extrai o texto do PDF
    text = extract_text_from_pdf(pdf_path)
    if "Erro:" in text:
        return text  # Retorna a mensagem de erro retornada pela função

    # Divide o texto em chunks
    chunks = split_text(text)

    # Cria o vectorstore
    vectorstore = create_vectorstore(chunks)

    # Responde à pergunta
    answer = answer_question(vectorstore, question, gemini_api_key)
    return answer

def gradio_interface():
    """
    Função para definir a interface do Gradio.
    """
    inputs = [
        gr.File(label="Caminho do Arquivo PDF"), # Campo para fazer upload do arquivo PDF
        gr.Textbox(label="Pergunta", placeholder="Insira sua pergunta sobre o PDF...") # Campo para inserir a pergunta
    ]
    outputs = gr.Textbox(label="Resposta", placeholder="A resposta à sua pergunta aparecerá aqui...") # Campo para exibir a resposta

    # Cria a interface do Gradio
    iface = gr.Interface(
        fn=main,
        inputs=inputs,
        outputs=outputs,
        title="AskMyPDF", # Título da interface
        description="Faça perguntas sobre o conteúdo do seu arquivo PDF.", # Descrição da interface
    )
    return iface

if __name__ == "__main__":
    iface = gradio_interface() # Cria a interface do Gradio
    iface.launch() # Inicia o servidor do Gradio
