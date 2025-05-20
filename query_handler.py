from vector_store import VectorStore
from pdf_parser import extract_text_from_pdf
import google.generativeai as genai

class QueryHandler:
    def __init__(self, gemini_api_key):
        genai.configure(api_key=gemini_api_key)
        self.vector_store = VectorStore()
        self.model = genai.GenerativeModel('gemini-pro')

    def process_pdf(self, file_path):
        text = extract_text_from_pdf(file_path)
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        self.vector_store.add_texts(chunks)

    def ask(self, question):
        context_chunks = self.vector_store.query(question)
        context = "\n".join(context_chunks)
        prompt = f"Com base apenas no seguinte conteúdo do PDF, responda a pergunta:\n\n{context}\n\nPergunta: {question}"
        response = self.model.generate_content(prompt)
        return response.text