import os
import fitz
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
from dotenv import load_dotenv
from google import genai

load_dotenv()

with open("apikey.txt", "r") as f:
    gemini_api_key = f.read().strip()

client = genai.Client(api_key=gemini_api_key)

chunk_size = 500
percentual_overlap = 0.2

def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        return text
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error: {e}"
    
arquivo = "teste.pdf"
texto = extract_text_from_pdf(arquivo)
filename = os.path.basename(arquivo)
metadados = {"nome do arquivo": filename}

text_splitter = CharacterTextSplitter(
    separator=".",
    chunk_size=chunk_size,
    chunk_overlap=int(chunk_size * percentual_overlap),
    length_function=len,
    is_separator_regex=False
)

all_splits = text_splitter.create_documents([texto], metadatas=[metadados])

for index, text in enumerate(all_splits):
    print(f"#### {index + 1} ####")
    print(text.page_content)
    print(text.metadata)

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(documents=all_splits, embedding=embedding)

question = "Sobre o que se trata o arquivo?"

docs = vectorstore.similarity_search_with_score(question, k=4)

context = "\n\n".join([doc[0].page_content for doc in docs])

prompt = f"""
Contexto extraído do documento:
{context}

Pergunta:
{question}
"""

# Usa o Gemini para gerar a resposta da pergunta com base no contexto
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print("Resposta Gemini:")
print(response.text)