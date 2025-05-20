from langchain.text_splitter import CharacterTextSplitter

def split_text(text, chunk_size=500, overlap=0.2):
    """
    Divide o texto em chunks menores para processamento.

    Args:
        text (str): O texto a ser dividido.
        chunk_size (int, opcional): O tamanho de cada chunk. Padrão é 500.
        overlap (float, opcional): A porcentagem de overlap entre os chunks. Padrão é 0.2.

    Returns:
        list: Uma lista de objetos Document, onde cada um contém um chunk do texto.
    """
    text_splitter = CharacterTextSplitter(
        separator=".",  # Separador para dividir o texto
        chunk_size=chunk_size,  # Tamanho máximo de cada chunk
        chunk_overlap=int(chunk_size * overlap),  # Tamanho do overlap entre os chunks
        length_function=len,  # Função para determinar o comprimento do texto (neste caso, usa o número de caracteres)
        is_separator_regex=False, # Indica se o separador é uma expressão regular
    )
    # Cria metadados para cada chunk, neste caso, apenas o nome do arquivo
    metadados = {"nome do arquivo": "nome_do_arquivo.pdf"}  # Você pode querer passar o nome do arquivo como argumento
    return text_splitter.create_documents([text], metadatas=[metadados])  # Retorna uma lista de Documentos

if __name__ == '__main__':
    texto_de_exemplo = "Este é um exemplo de texto longo. Ele será dividido em chunks menores. Cada chunk terá um tamanho máximo de 500 caracteres. Haverá um overlap de 20% entre os chunks. O separador usado será o ponto final."
    chunks = split_text(texto_de_exemplo)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk.page_content}")