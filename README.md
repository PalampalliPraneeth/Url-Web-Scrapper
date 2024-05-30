# 🌐 Smart Web Scraper Q&A with Gemini LLM 🦙🦜

This project is a web-based application built with Streamlit that allows users to scrape text content from a URL and ask questions about the content using a custom LLM (Language Learning Model) based on Gemini. The application uses modern NLP techniques to process and retrieve relevant information from the scraped content.

## Features

- **Web Scraping**: Fetches and processes text content from a provided URL.
- **Question Answering**: Utilizes a custom LLM (Gemini) to answer user queries based on the scraped content.
- **User-Friendly Interface**: Simple and intuitive interface built with Streamlit.
- **Interactive Visuals**: Styled with custom CSS for a better user experience.

## Installation

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
