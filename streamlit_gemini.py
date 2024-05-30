import os
import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.schema import HumanMessage
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain_core.language_models.llms import LLM
from typing import Any, List, Mapping, Optional

class Tool:
    def __init__(self, name, func, description, coroutine=None):
        self.name = name
        self.func = func
        self.description = description
        self.coroutine = coroutine
        self.is_single_input = True

class GeminiLLM(LLM):

    @property
    def _llm_type(self) -> str:
        return "gemini"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        api_key = os.getenv('GEMINI_API_KEY')  # Ensure your API key is set in the environment variables
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyC7VNSANzB0863NIKGzL1mal66grwTcxCg"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status() 

        response_json = response.json()
        print("Response JSON:", response_json) 

        assistant_message = response_json['candidates'][0]['content']['parts'][0]['text']
        return assistant_message

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {}

def fetch_text_from_url(url: str) -> str:
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    return text

def custom_css():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            border: none;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .output-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            transition: 0.3s;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    custom_css()

    st.title("🌐 Smart Web Scraper Q&A with Gemini LLM 🦙🦜")

    st.sidebar.header("Input Your URL and Question")

    with st.sidebar.form(key='input_form'):
        url = st.text_input("Enter URL:", "")
        query = st.text_input("Enter your question:", "")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button and url and query:
        with st.spinner("Fetching and processing text..."):
            text = fetch_text_from_url(url)
            document = Document(page_content=text, metadata={"url": url})

            r_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = r_splitter.split_text(document.page_content)
            model = SentenceTransformer('all-MiniLM-L6-v2')

            embeddings = model.encode(chunks)

            llm = GeminiLLM()

            chain = load_qa_chain(llm, chain_type="stuff")

            inputs = {"query": query, "question": query, "input_documents": [Document(page_content=chunk) for chunk in chunks]}

            with st.spinner("Getting the answer..."):
                result = chain.invoke(inputs)
                st.success("Answer retrieved!")

                with st.container():
                    st.markdown("### 📝 Question")
                    st.write(query)

                    st.markdown("### 📘 Answer")
                    st.write(result)
    elif submit_button:
        st.error("Please enter both a URL and a question.")

if __name__ == "__main__":
    main()
