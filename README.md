# Projeto para disciplina de Inteligencia Artifical

Projeto com o objetivo de estudar e compreender as diferenças entre LLMs e discutir seus resultados, ou seja, programação em pares com LLMs.

# LLM utilizada
 - Gemini 2.0 Flash: Corrigir erros e implementar funções.

 - Gemini 1.5 Flash: Saídas para perguntas sobre PDF carregado.

# Funcionalidades:
 - Upload de PDF.

 - Processamento e extração de texto do PDF.

 - Indexação dos dados em um sistema vetorial (ex: FAISS).

 - Interface web para interação.

 - Resposta baseada no conteúdo do PDF.

# Projeto da solução

## Arquitetura do projeto

```
Usuário ↔ Interface (Gradio) ↔ Módulo de Processamento de PDF ↔ Indexador (Embeddings + Chroma) ↔ RAG ↔ LLM (Gemini) ↔ Resposta
```

## Módulos 
- `app.py`: Define a interface do usuário com Gradio. Coordena o fluxo de dados entre os módulos. Carrega a chave da API do Gemini.

- `pdf_processor.py`: Responsável por extrair o texto do arquivo PDF usando PyMuPDF (`fitz`)

 - `text_splitter.py`: Divide o texto extraído em chunks menores usando `CharacterTextSplitter` do Langchain.

 - `vector_store.py`: Cria o banco de dados vetorial (Chroma) a partir dos chunks de texto e os embeddings gerados pelo Hugging Face.

 - `question_answerer.py`: Contém a lógica para responder às perguntas usando o modelo Gemini, o banco de dados vetorial e o padrão RAG (Retrieval Augmented Generation).

 - `requirements.txt`: Lista as dependências do projeto (Langchain, Gradio, PyPDF2, etc.). Use `pip install -r requirements.txt` para instalar.

 - `apikey.txt`: Arquivo para armazenar a chave de API do Gemini.

## Fluxo
 1. O usuário carrega um arquivo PDF e insere uma pergunta na interface do Gradio.

 2. O sistema extrai o texto do PDF usando o módulo `pdf_processor.py`.

 3. O texto é dividido em chunks menores pelo módulo `text_splitter.py`.

 4. Embeddings são gerados para os chunks e armazenados no banco de dados vetorial Chroma usando o módulo `vectorstore.py`.

 5. Quando o usuário faz uma pergunta, o sistema recupera os chunks mais relevantes do banco de dados vetorial.

 6. Um prompt é criado com os chunks recuperados e enviado para o modelo Gemini (via `question_answerer.py`).

 7. O modelo Gemini gera a resposta, que é exibida na interface do Gradio.

# Programação em pares

Durante a implementação, foi utilizada uma LLM, Gemini 2.0 Flash como parceiro de programação para escrever código, analisar problemas e realizar alterações conforme solicitado.

# Testes
 - Testes unitários para cada módulo (`pdf_processor.py`, `vectorstore.py`, etc.).

 - Testes de integração (fluxo completo: PDF → pergunta → resposta).

## Casos de teste:

 - PDF técnico com termos específico

 - Perguntas fora do escopo (espera-se uma resposta do tipo “não sei”)

 - Perguntas diretas, indiretas, multi-sentença

