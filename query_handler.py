from vector_store import VectorStore
from pdf_parser import extract_text_from_pdf
import openai
import os

class QueryHandler:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
        self.vector_store = VectorStore()

    def process_pdf(self, file_path):
        text = extract_text_from_pdf(file_path)
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        self.vector_store.add_texts(chunks)

    def ask(self, question):
        context_chunks = self.vector_store.query(question)
        context = "\n".join(context_chunks)

        system_message = "Você é um assistente útil que responde perguntas usando somente o conteúdo do PDF fornecido."
        user_message = f"Baseie sua resposta apenas neste conteúdo:\n\n{context}\n\nPergunta: {question}"

        response = openai.ChatCompletion.create(
            model="gpt-4",  # ou "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0,
            max_tokens=500,
        )

        return response.choices[0].message['content'].strip()
