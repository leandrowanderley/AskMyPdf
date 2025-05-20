import gradio as gr
from query_handler import QueryHandler

handler = QueryHandler(gemini_api_key="SUA_CHAVE_GEMINI")

def upload_pdf(file):
    handler.process_pdf(file.name)
    return "PDF carregado com sucesso."

def ask_question(question):
    return handler.ask(question)

with gr.Blocks() as demo:
    gr.Markdown("# Chat com seu PDF")
    with gr.Row():
        pdf_input = gr.File(label="Envie um PDF")
        upload_button = gr.Button("Carregar PDF")
    upload_status = gr.Textbox(label="Status")
    upload_button.click(upload_pdf, inputs=pdf_input, outputs=upload_status)

    question_input = gr.Textbox(label="Faça uma pergunta")
    answer_output = gr.Textbox(label="Resposta")
    ask_button = gr.Button("Perguntar")
    ask_button.click(ask_question, inputs=question_input, outputs=answer_output)

demo.launch()