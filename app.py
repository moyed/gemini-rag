import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_core.prompts import ChatPromptTemplate

import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
st.set_page_config(page_title="Chat with multiple PDF")  

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            pdf_doc = page.extract_text()
            text += pdf_doc
    return text

def get_text_chunks(text):
    spilliter = RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=100)
    text_chunks = spilliter.split_text(text)
    print("Extracted PDF text:", text_chunks)
    return text_chunks

def get_vectore_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks,embedding=embeddings)
    vector_store.save_local("faiss_index")

def load_vector_index(allow_deserialization=False):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=allow_deserialization
    )
    return new_db
 
def create_llm():
    """Create the Chat LLM (Google's Gemini) instance."""
    return ChatGoogleGenerativeAI(
        api_key=os.getenv("GOOGLE_API_KEY"),
        model="gemini-2.0-flash-exp",
        temperature=0.7,
        max_tokens=20000
    )

def get_prompt_template():
    return """
    Answer the following question from the provided context. 
    Provide the answer in the context of the text.
    If the answer is not in the text, write "Answer not in text".
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """

def user_input(user_question):
    new_db = load_vector_index(allow_deserialization=True)

    docs = new_db.similarity_search(user_question, k=10)

    # 2. Convert docs to a single string (if you only use one doc, it's docs[0])
    context_str = "\n".join([doc.page_content for doc in docs])
    print("context_str (preview):", context_str[:300], "..." if len(context_str) > 300 else "")

    # 3. Create Chat LLM
    llm = create_llm()

    # 4. Build Prompt Template
    prompt_template = get_prompt_template()

    prompt = ChatPromptTemplate.from_messages([("human", prompt_template)])
    print("user_question:", user_question)


    rag_chain = prompt | llm

# 2. Invoke the chain with your dictionary
    response = rag_chain.invoke({"context": context_str, "question": user_question})

    # 7. Output
    st.write("Reply:", response.content)
    print("DEBUG:", response.content)
    
def main():
    st.title("Upload PDFs")
    st.header("Chat with PDF using Gemini")


    with st.sidebar:
        st.title("Menu")
        st.write("This is a demo of a conversational chain using Gemini and FAISS.")
        st.write("Upload PDFs and ask questions about the content of the PDFs.")
        st.write("The model will try to answer the question based on the content of the PDFs.")
        st.write("If the answer is not in the text, the model will respond with 'Answer not in text'.")
    pdf_docs = st.file_uploader("Upload PDFs and Click on Submit", type=["pdf"], accept_multiple_files=True)
    if pdf_docs:
        if st.button("Submit & Process"):
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vectore_store(text_chunks)
                    st.success("Processing Done!")
    else:
        st.warning("Please upload PDFs to continue.")
                
    user_question = st.text_input("Enter your question:")

    if user_question:
        with st.spinner("Generating answer..."):
            answer = user_input(user_question)
            st.write("Reply:", answer)

        

                
if __name__ == "__main__":
    main()