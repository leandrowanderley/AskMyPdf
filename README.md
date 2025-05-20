# Projeto para disciplina de Inteligencia Artifical

Projeto com o objetivo de estudar e compreender as diferenças entre LLMs e discutir seus resultados, ou seja, programação em pares com LLMs.

# LLM utilizada
- ChatGPT

# Funcionais:
- Upload de PDF.

- Processamento e extração de texto do PDF.

- Indexação dos dados em um sistema vetorial (ex: FAISS).

- Interface de chat para interação.

- Resposta baseada no conteúdo do PDF.

# Não-funcionais:
- Tempo de resposta aceitável (≤ 5s).

- Interface intuitiva.

- Registro de interações e respostas para fins de relatório.

# Projeto da solução

# # Arquitetura do projeto

```
Usuário ↔ Interface ↔ Módulo PDF ↔ Indexador (Embeddings + Vector DB) ↔ RAG ↔ LLM ↔ Resposta
```

# # Módulos 
- pdf_parser.py: responsável por extrair texto do PDF.

- vector_store.py: armazena e consulta o conteúdo embeddado.

- query_handler.py: cuida do pipeline RAG (pergunta → busca → contexto → resposta).

- app.py: interface do usuário.

- requirements.txt: requisitos para rodar o sistema, e utilizando (pip install) instala.

# # Fluxo
1. Usuário envia um PDF.

2. Sistema extrai texto e divide em chunks.

3. Gera embeddings e armazena no banco vetorial.

4. Usuário faz uma pergunta.

5. Sistema recupera os chunks mais relevantes via similaridade vetorial.

6. Gera prompt com os chunks e envia ao LLM.

7. Retorna resposta ao usuário.

# Programação em pares

Durante a implementação foi utilizado uma LLM como dupla, onde a LLM escreve o código, análisa, e realiza mudanças no código que eu pedir, como otimização do código.

# Testes
Testes unitários para cada módulo (pdf_parser, vector_store, etc.)

Testes de integração (ciclo completo: PDF → pergunta → resposta)

Casos de teste:

 - PDF técnico com termos específicos

 - Perguntas fora do escopo (espera-se uma resposta do tipo “não sei”)

 - Perguntas diretas, indiretas, multi-sentença

