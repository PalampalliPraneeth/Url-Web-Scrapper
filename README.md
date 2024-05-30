# 🌐 Smart Web Scraper Q&A with Gemini LLM 🦙🦜

This project is a web-based application built with Streamlit that allows users to scrape text content from a URL and ask questions about the content using a LLM (Language Learning Model) based on Gemini and Langchain agents. The application utilizes the Gemini LLM (Large Language Model) from Google to provide accurate and relevant answers to the user's questions.

## 🚀 Features

- **Web Scraping**: Fetches and processes text content from a provided URL.
- **Text Processing**: Split the text into smaller chunks for efficient processing.
- **Question Answering**: Utilizes a custom LLM (Gemini) to answer user queries based on the scraped content.
- **User-Friendly Interface**: Simple and intuitive interface built with Streamlit.
- **Interactive Visuals**: Styled with custom CSS for a better user experience.

## 🤖 LangChain Agents 

This project leverages LangChain agents, which are a powerful feature of the LangChain library. Agents are designed to combine various tools and LLMs to accomplish more complex tasks. In this application, the agent is responsible for orchestrating the entire process of fetching text from a URL, processing it, and answering user questions using the Gemini LLM.

The agent utilizes the following tools:

- **Web Scraper Tool**: This tool fetches the text content from a given URL using web scraping techniques.
- **Text Splitter Tool**: This tool splits the fetched text into smaller chunks for efficient processing and embedding.
- **Embeddings Tool**: This tool encodes the text chunks into embeddings using the Sentence Transformers library.
- **Question Answering Tool**: This tool takes the user's question and the encoded text chunks as input, and provides an answer using the Gemini LLM.

By combining these tools, the agent can seamlessly handle the entire workflow, from fetching text to providing accurate answers to user questions.


## 🛠️ Installation

To get started with the application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/smart-web-scraper-qa.git
   cd smart-web-scraper-qa
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Streamlit secrets**:
   Add your Gemini API key to the .streamlit/secrets.toml file:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```
4. **🚀 Run the application**:
   ```bash
   streamlit run streamlit_gemini.py
   ```
## 📦 Dependencies 

This project relies on the following libraries:

- `streamlit`: For building the user interface.
- `requests`: For making HTTP requests to fetch the URL content.
- `beautifulsoup4`: For parsing the HTML content and extracting text.
- `langchain`: For text processing and question answering using the Gemini LLM.
- `sentence-transformers`: For encoding the text chunks into embeddings.
- `faiss-cpu`: For efficient vector similarity search.

## 🤝 Contributing 

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## 🙏 Acknowledgements 

This project utilizes the following resources:

- [Streamlit](https://streamlit.io/): An open-source app framework for building data apps.
- [LangChain](https://github.com/hwchase17/langchain): A framework for building applications with large language models.
- [Sentence Transformers](https://github.com/UKPLab/sentence-transformers): A library for encoding text into embeddings.
- [Gemini LLM](https://cloud.google.com/vertex-ai/docs/generative-ai/tutorials/text-generation): Google's Generative Language Model for text generation.
