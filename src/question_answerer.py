from langchain.prompts import PromptTemplate
from langchain_core.runnables import chain, RunnablePassthrough as LCRunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

def configure_genai(api_key, model_name="gemini-1.5-flash"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name=model_name,
        generation_config={
            "temperature": 0.8,
            "top_p": 0.9,
            "top_k": 50,
            "max_output_tokens": 4000,
            "response_mime_type": "text/plain",
        }
    )

def answer_question(vectorstore, question, gemini_api_key):
    # No need to configure genai here again if you're passing the key directly
    # genai.configure(api_key=gemini_api_key)

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, google_api_key=gemini_api_key)

    template = """Contexto:
    {context}

    Pergunta:
    {question}"""
    prompt = PromptTemplate.from_template(template)

    retrieval_chain = (
        {"context": vectorstore.as_retriever(search_kwargs={"k": 3}), "question": chain.LCRunnablePassthrough()}
        | prompt
        | model
    )

    response = retrieval_chain.invoke(question)
    return response.content

if __name__ == '__main__':
    print("Sim")