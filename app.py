from query_handler import QueryHandler

def main():
    with open("apikey.txt", "r") as f:
        apikey = f.read().strip()
    handler = QueryHandler(openai_api_key=apikey)

    pdf_path = input("Digite o caminho do arquivo PDF: ").strip()
    try:
        handler.process_pdf(pdf_path)
        print("PDF carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o PDF: {e}")
        return

    while True:
        question = input("\nFaça uma pergunta (ou digite 'sair' para encerrar): ").strip()
        if question.lower() == "sair":
            print("Encerrando o programa.")
            break
        try:
            resposta = handler.ask(question)
            print(f"Resposta: {resposta}")
        except Exception as e:
            print(f"Erro ao obter resposta: {e}")

if __name__ == "__main__":
    main()
