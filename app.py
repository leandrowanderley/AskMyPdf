import os
from dotenv import load_dotenv
from src.pdf_processor import extract_text_from_pdf
from src.text_splitter import split_text
from src.vectorstore import create_vectorstore
from src.question_answerer import answer_question

load_dotenv()

def main():
    """
    Função principal para executar o aplicativo de perguntas e respostas sobre PDF.
    """
    with open("apikey.txt", "r") as f:
        gemini_api_key = f.read().strip() # Carrega a chave da API do arquivo .env
    if not gemini_api_key:
        print("Erro: Chave da API do Gemini não encontrada no arquivo .env ou como variável de ambiente.")
        return

    pdf_path = input("Por favor, insira o caminho para o arquivo PDF: ")
    question = input("Por favor, insira sua pergunta: ")

    # Extrai o texto do PDF
    text = extract_text_from_pdf(pdf_path)
    if "Erro:" in text:
        print(text)  # Exibe a mensagem de erro retornada pela função
        return

    # Divide o texto em chunks
    chunks = split_text(text)

    # Cria o vectorstore
    vectorstore = create_vectorstore(chunks)

    # Responde à pergunta
    answer = answer_question(vectorstore, question, gemini_api_key)
    print("\nResposta:")
    print(answer)

if __name__ == "__main__":
    main()