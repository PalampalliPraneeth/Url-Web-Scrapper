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
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyC7VNSANzB0863NIKGzL1mal66grwTcxCg"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes

        response_json = response.json()
        print("Response JSON:", response_json)  # Debugging statement

        # Adjust parsing logic based on actual response structure
        # Example placeholder, this needs to be updated according to the actual response JSON
        # assistant_message = response_json['candidates'][0]['output']['parts'][0]['text']
        
        # Returning a dummy message until actual structure is known
        assistant_message = response_json['candidates'][0]['content']['parts'][0]['text']
        return assistant_message

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {}

# Fetch data from the URL using BeautifulSoup
url = "https://www.nbcnews.com/news/world/india-issues-heat-wave-alert-delhi-hits-122-degrees-rcna154439"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text()

# Define a class to represent the document
class MyDocument:
    def __init__(self, text, metadata=None):
        self.page_content = text
        self.metadata = metadata or {}

# Create a document object
document = MyDocument(text, metadata={"url": url})

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Split the text into smaller chunks
r_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = r_splitter.split_text(document.page_content)

# Embed the chunks
embeddings = model.encode(chunks)

# Initialize the GeminiLLM
llm = GeminiLLM()

# Create the QA chain
chain = load_qa_chain(llm, chain_type="stuff")

# Ask a question
query = "what is highest temperature recorded?"
inputs = {"query": query, "question": query, "input_documents": [Document(page_content=chunk) for chunk in chunks]}
# Get the answer
result = chain.invoke(inputs)
print(result)
