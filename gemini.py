import os
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
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status() 

        response_json = response.json()
        print("Response JSON:", response_json)  # Debugging statement

        assistant_message = response_json['candidates'][0]['content']['parts'][0]['text']
        return assistant_message

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {}

url = "https://www.nbcnews.com/news/world/india-issues-heat-wave-alert-delhi-hits-122-degrees-rcna154439"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text()

class MyDocument:
    def __init__(self, text, metadata=None):
        self.page_content = text
        self.metadata = metadata or {}

document = MyDocument(text, metadata={"url": url})

model = SentenceTransformer('all-MiniLM-L6-v2')

r_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = r_splitter.split_text(document.page_content)

embeddings = model.encode(chunks)

llm = GeminiLLM()

chain = load_qa_chain(llm, chain_type="stuff")

query = "what is highest temperature recorded?"
inputs = {"query": query, "question": query, "input_documents": [Document(page_content=chunk) for chunk in chunks]}
result = chain.invoke(inputs)
print(result)
