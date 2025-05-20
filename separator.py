import os
import fitz
from langchain.text_splitter import CharacterTextSplitter

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

texts = text_splitter.create_documents([texto], metadatas=[metadados])

for index, text in enumerate(texts):
    print(f"#### {index + 1} ####")
    print(text.page_content)
    print(text.metadata)
