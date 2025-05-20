import fitz  # Importa a biblioteca fitz (PyMuPDF)

def extract_text_from_pdf(file_path):
    """
    Extrai o texto de um arquivo PDF.

    Args:
        file_path (str): O caminho para o arquivo PDF.

    Returns:
        str: O texto extraído do PDF, ou uma mensagem de erro se ocorrer algum problema.
    """
    try:
        doc = fitz.open(file_path)  # Abre o arquivo PDF usando o PyMuPDF
        text = ""
        for page in doc:  # Itera sobre cada página do documento
            text += page.get_text() + "\n"  # Obtém o texto da página e adiciona à variável `text`
        doc.close()  # Fecha o documento PDF
        return text  # Retorna o texto extraído
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."  # Retorna mensagem de erro se o arquivo não for encontrado
    except Exception as e:
        return f"Erro: {e}"  # Retorna mensagem de erro genérica com detalhes da exceção
    
if __name__ == '__main__':
    # Você pode adicionar um teste aqui se quiser executar este arquivo diretamente
    pdf_path = "seu_arquivo.pdf"  # Substitua pelo caminho do seu arquivo de teste
    texto = extract_text_from_pdf(pdf_path)
    if "Erro:" in texto:
        print(texto)
    else:
        print(texto[:100]) #imprime os primeiros 100 caracteres